from vncdotool import api
import threading
from time import sleep
import time
import socket
import os
from datetime import datetime, timedelta


screenshot_path = "static/"
active_threads = {}
last_thread_creation_time = {}
def is_screen_active(port,host="127.1.1.0",timeout=2):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #presumably 
    sock.settimeout(timeout)
    try:
       sock.connect((host,port))
    except:
       return False
    else:
       sock.close()
       return True

def capture_screenshot(host="127.1.1.0",port=5505):
    connectTo = host+"::"+str(port)
    isHostActive = is_screen_active(port,host)
    print(isHostActive)
    while isHostActive:# and not termination_flag:
        isHostActive = is_screen_active(port,host)
        try:
            print("Getting screenshot of",port)

            client = api.connect(connectTo)
            current_time = time.time()
            sleep_duration = 2 - (current_time % 2)  # Adjust 2 to the desired even interval
            sleep(sleep_duration)
            isHostActive = is_screen_active(port,host)
            if isHostActive:
                client.refreshScreen()
                client.captureScreen(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png",True)
                client.disconnect()


            sleep(1)  # Wait for 3 seconds before refreshing the screenshot
        except:
            pass    
    try:
        if os.path.exists(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png"):
            print("Deleted Off")
            os.remove(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png")
    except:
        sleep(.2)
        if os.path.exists(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png"):
            print("Deleted Off")
            os.remove(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png")
    del active_threads[port]





def start_thread(host,port):
    if port not in active_threads or not active_threads[port].is_alive():
        # Start a new thread if the port is not in use or the thread is not alive
        active_threads[port] = threading.Thread(target=capture_screenshot, args=(host, port))
        active_threads[port].start()
        last_thread_creation_time[port] = time.time()
        print(f"Thread started for {host}:{port}")
    elif time.time() - last_thread_creation_time.get(port, 0) > 300:  # 300 seconds = 5 minutes
        # Start a new thread if the existing thread has been running for more than 5 minutes
        active_threads[port] = threading.Thread(target=capture_screenshot, args=(host, port))
        active_threads[port].start()
        last_thread_creation_time[port] = time.time()
        print(f"Thread restarted for {host}:{port}")
    else:
        print(f"Thread for {host}:{port} is already running")

def deleteImages(host,port):
        if os.path.exists(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png"):
            creation_time = datetime.fromtimestamp(os.path.getctime(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png"))
            current_time = datetime.now()
            age = current_time - creation_time
            if age > timedelta(minutes=2):
                print("Deleted Off")
                try:
                    os.remove(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png")
                except:
                    sleep(.2)
                    if os.path.exists(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png"):
                        print("Deleted Off")
                        os.remove(screenshot_path+host.replace(".","")+"-"+str(port)[-3:]+".png")


while True:
    for i in range(30): #a cada 10s*6(1m)*10(10m)*6(60m) deletar as imagens
        for port in range(5501, 5699):
            
            if port in active_threads:
                print("skip",port)
            else:
                try:
                    start_thread("127.1.1.0",port)
                except:
                    pass
        host = "127.1.1.0"
        sleep(5)
        try:
            for port in active_threads:
                isHostActive = is_screen_active(port,host)
                if not isHostActive:
                    deleteImages(host,port)
                    # del active_threads[port]
                    print("deletadas",port)
        except:
            pass

        sleep(5)
