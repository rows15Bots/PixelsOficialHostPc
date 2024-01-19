import subprocess
import signal
from flask import Flask, render_template, send_from_directory, jsonify, after_this_request
import os
import socket
import concurrent.futures
from time import sleep
import threading
import random
import psutil
import gc
app = Flask(__name__)

def start_websockify(vnc_host, vnc_port, websockify_port):
    websockify_cmd = [
        "websockify",
        f":{websockify_port}",
        f"{vnc_host}:{vnc_port}"
    ]
    return subprocess.Popen(websockify_cmd)

def is_screen_active(port,host="127.1.1.0",timeout=.5):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #presumably 
    sock.settimeout(timeout)
    try:
       sock.connect((host,port))
    except Exception:
       sock.close()
       return False
    else:
       sock.close()
       return True

def check_ports_range(start, end, hosts, max_workers=300):
    active_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Use executor.map to parallelize the execution of is_screen_active for each host and port
        futures = {executor.submit(is_screen_active, port, host): (port, host) for host in hosts for port in range(start, end)}
        for future in concurrent.futures.as_completed(futures):
            port, host = futures[future]
            try:
                if future.result():
                    #TEMP
                    if port != 5040:
                        active_ports.append((host, port))
                        print(host,port)
            except Exception as e:
                print(f"Error checking port {port} on host {host}: {e}")
    return active_ports

# Define the range of ports to check

start_port = 5001
end_port = 5200
VncConnections = []
# Define the list of hosts
hosts = [
    "192.168.0.25", 
    # "192.168.0.31", 
    # "192.168.0.33", 
    "192.168.0.34", 
    "192.168.0.35", 
    "192.168.0.36", 
    "192.168.0.50",
    "192.168.0.53",
    "192.168.0.54",
    "192.168.0.57", 
    ]
def custom_sort(item):
    return (item[0], item[1])


base_port = 29500
currport = 29500
websockify_processes = []
def getWebsocket(vnc_host,vnc_port):
    global base_port
    global currport
    global VncConnections
    global VncHostsAndPorts
    if currport > 30000:
        currport = base_port
    currport +=1
    websockify_port = currport
    process = start_websockify(vnc_host, vnc_port, websockify_port)
    websockify_processes.append([process,vnc_host,vnc_port])
    return websockify_port

# @app.route('/refresh')
# def closeWs():
#     return render_template('blankhtml.html')
# portsChecker_thread = None
# def portsCheckerThreadStarter():
#         portsChecker_thread = threading.Thread(target=portsChecker)
#         portsChecker_thread.start()
def portsChecker(hostsArg=False):
    global websockify_processes
    global VncConnections
    global VncHostsAndPorts
    
    print("STARTED THREAD")
    # while True:
    if hostsArg == True:
        
        hostsTemp = [
            # "192.168.0.25", 
            # "192.168.0.31", 
            # "192.168.0.33", 
            "192.168.0.34", 
            "192.168.0.35", 
            "192.168.0.36", 
            "192.168.0.50",
            "192.168.0.53",
            "192.168.0.54",
            "192.168.0.57", 
            ]
        VncConnections = check_ports_range(5899, 5901, hostsTemp, max_workers=3000)
    else:
        VncConnections = check_ports_range(start_port, end_port, hosts, max_workers=3000)
    sorted_VncConnections = sorted(VncConnections, key=custom_sort)
    host_name_list = [
        ['192.168.0.57', 'SVI7'],
        ['192.168.0.34', 'SVXEON'],
        ['192.168.0.25', 'PCZAO'],
        ['192.168.0.35', 'NITRO.'],
        ['192.168.0.36', 'NITRO'],
        ['192.168.0.50', 'RIG1'],
        ['192.168.0.54', 'RIG2'],
        ['192.168.0.53', 'RIG3'],
                      ]
    host_name_dict = {ip: name for ip, name in host_name_list}
    VncHostsAndPorts = [(ip, port, host_name_dict.get(ip, ip)) for i, (ip, port) in enumerate(sorted_VncConnections)]

# @app.route('/<ip>/<int:port>')
# def serve_ip_and_port(ip, port):
#     portsChecker()
#     refreshIps()
#     print(VncConnections)
#     print(VncHostsAndPorts)
#     solovm = []
#     for vnhostandport in VncHostsAndPorts:
#         if ip == vnhostandport[0] and port == vnhostandport[1]:
#             solovm.append(vnhostandport)
#     print(f'Serving IP: {ip}, Port: {port}')
#     return render_template('inputvm.html',servers=solovm)

VncHostsAndPorts = []

def clean_websockify_processes():
    global VncHostsAndPorts
    global websockify_processes
    simplifiedHosts = []
    for vncHost in VncHostsAndPorts:
        simplifiedHosts.append([vncHost[0],vncHost[1]])
    for x in websockify_processes:
        process,host,port = x
        if [host,port] not in simplifiedHosts:
            print(host,port)
            try:
                process.kill()
                process.terminate()
            except Exception as e:
                print(e)
                pass


    


@app.route('/check')
def checkProcs():
    
    return [len(websockify_processes)]
@app.route('/kill')
def killProcs():
    clean_websockify_processes()
    return [len(websockify_processes)]
@app.route('/allvms')
def index():
    
    return render_template('indexv2.html')
@app.route('/allvms_obs')
def indexv2_obs():
    
    return render_template('indexv2_obs.html')
@app.route('/hosts')
def hostsPage():
    
    return render_template('hostsv2.html')

@app.route('/get_servers_hosts')
def get_servers_hosts():
    global VncHostsAndPorts
    clean_websockify_processes()
    portsChecker(hostsArg=True)
    sleep(1)
    return jsonify(servers=VncHostsAndPorts)


@app.route('/get_servers')
def get_servers():
    global VncHostsAndPorts
    clean_websockify_processes()
    portsChecker()
    sleep(1)
    # Simulating updated data
    updated_servers = [
        ('192.168.0.34', 5004, 'NETRO2.'),
        ('192.168.0.34', 5008, 'NETRO2.'),
        ]
    # VncHostsAndPorts
    
    
    gc.collect()
    return jsonify(servers=VncHostsAndPorts)

@app.route('/get_websocketport/<ip>/<int:port>')
def get_websocketport(ip,port):
    
    port = getWebsocket(ip,port)
    sleep(.2)
    return jsonify(wsports=port)

@app.route('/allvms/<path:filename>')
def serve_rfb_js(filename):
    return send_from_directory(os.path.join(app.root_path), filename, mimetype='application/javascript')

@app.route('/<ip>/<int:port>')
def serve_ip_and_port(ip,port):
    return render_template('inputvmv2.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4999)








    # try:
    # finally:
    #     # Ensure websockify process is terminated when the Flask app exits
    #     websockify_process.terminate()
    #     websockify_process.wait()  # Wait for the process to finish

# Define a signal handler to gracefully terminate the websockify process
# def handle_termination_signal(signum, frame):
#     print("Received termination signal. Stopping websockify...")
#     websockify_process.terminate()
#     websockify_process.wait()  # Wait for the process to finish
#     print("Websockify stopped. Exiting...")
#     exit(0)

# # Register the signal handler for termination signals
# signal.signal(signal.SIGTERM, handle_termination_signal)
# signal.signal(signal.SIGINT, handle_termination_signal)  # Handle Ctrl+C





# active_ports_list = check_ports_range(start_port, end_port, hosts, max_workers=100)
# print(active_ports_list)