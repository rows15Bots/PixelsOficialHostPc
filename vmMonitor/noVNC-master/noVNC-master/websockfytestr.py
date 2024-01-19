import subprocess
import signal
from flask import Flask, render_template, send_from_directory
import os
import socket
import concurrent.futures
from time import sleep
from websockify.websocketproxy import WebSocketProxy

app = Flask(__name__)

def start_websockify(vnc_host, vnc_port, websockify_port):
    websockify_cmd = [
        "websockify","--run-once",
        f":{websockify_port}",
        f"{vnc_host}:{vnc_port}"
    ]
    websockify_process = subprocess.Popen(websockify_cmd)
    return websockify_process

# def start_websockify(vnc_host, vnc_port, websockify_port):
#     websockify_process = WebSocketProxy(run_once=True, timeout=30, idle_timeout=60, target_host=vnc_host, target_port=vnc_port, listen_port=websockify_port,
#              daemon=True).start_server()
#     return websockify_process




def is_screen_active(port,host="127.1.1.0",timeout=.5):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #presumably 
    sock.settimeout(timeout)
    try:
       sock.connect((host,port))
    except:
       return False
    else:
       sock.close()
       return True

def check_ports_range(start, end, hosts, max_workers=2000):
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
            except Exception as e:
                print(f"Error checking port {port} on host {host}: {e}")
    return active_ports

# Define the range of ports to check
start_port = 5001
end_port = 5301

# Define the list of hosts
hosts = [
    "192.168.0.57", 
    # "192.168.0.31", 
    # "192.168.0.33", 
    "192.168.0.34", 
    # "192.168.0.36", 
    # "192.168.0.50",
    # "192.168.0.54",
    ]


# VncConnections = [('192.168.0.57', 5900), ('192.168.0.57', 5008)]
# VncConnections = check_ports_range(start_port, end_port, hosts, max_workers=100)
# print(VncConnections)
# sleep(1)



base_port = 29500
# VncHostsAndPorts = [(host, port, base_port + i) for i, (host, port) in enumerate(VncConnections)]
VncHostsAndPorts = []


websockify_processes = []
# websockify_processes = []

# for vnc_host, vnc_port, websockify_port in VncHostsAndPorts:
#     process = start_websockify(vnc_host, vnc_port, websockify_port)
#     websockify_processes.append(process)

def custom_sort(item):
    return (item[0], item[1])

def refreshIps():
    global websockify_processes
    global VncConnections
    global VncHostsAndPorts
    VncConnections = check_ports_range(start_port, end_port, hosts, max_workers=100)
        # websockify_process.wait()  # Wait for the process to finish
    base_port = 29500
    sleep(1)
    sorted_VncConnections = sorted(VncConnections, key=custom_sort)
    VncHostsAndPorts = [(host, port, base_port + i) for i, (host, port) in enumerate(sorted_VncConnections)]
    websockify_processes = []
    for vnc_host, vnc_port, websockify_port in VncHostsAndPorts:
        process = start_websockify(vnc_host, vnc_port, websockify_port)
        websockify_processes.append(process)

# @app.route('/close')
# def closeWs():
#     global websockify_processes
#     print(websockify_processes)
#     for websockify_process in websockify_processes:
#         print('closing',websockify_process)
#         websockify_process.terminate()
#         websockify_process.wait()  
#     return render_template('blankhtml.html')

@app.route('/')
def index():
    refreshIps()
    print(VncConnections)
    print(VncHostsAndPorts)
    return render_template('index.html',servers=VncHostsAndPorts)

@app.route('/<path:filename>')
def serve_rfb_js(filename):
    return send_from_directory(os.path.join(app.root_path), filename, mimetype='application/javascript')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
        
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