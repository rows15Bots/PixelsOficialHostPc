from vncdotool import api
import threading
from time import sleep
import time
import socket
import os
from datetime import datetime, timedelta


screenshot_path = "static/"
sharedFolderPath = "C:\VmSharedFolder"
offFile = r"off.txt"
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
    client = None
    connectTo = host+"::"+str(port)
    isHostActive = is_screen_active(port,host)
    if isHostActive:
        print(isHostActive,port)
        name = screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]
    while isHostActive and not getOffInfoFromFolder(sharedFolderPath,port):# and not termination_flag:
        isHostActive = is_screen_active(port,host)
        try:
            client = api.connect(connectTo)
            print("Getting screenshot of",port)
            current_time = time.time()
            sleep_duration = 1 - (current_time % 1)  # Adjust 2 to the desired even interval
            # sleep_duration = .5
            sleep(sleep_duration)
            isHostActive = is_screen_active(port,host)
            if isHostActive:
                if not getOffInfoFromFolder(sharedFolderPath,port):
                    client.refreshScreen()
                    client.captureScreen(name+".png",True)
                    client.disconnect()
                    sleep(.1)


            sleep(.1)  # Wait for 3 seconds before refreshing the screenshot
        except:
            pass    
    # if client:
    # print("sai da thread", isHostActive ,getOffInfoFromFolder(sharedFolderPath,port))
    try:
        try:
            del active_threads[port]
        except:
            pass
        if os.path.exists(screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]+".png"):
            print("Deleted Off",port)
            os.remove(screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]+".png")
    except:
        sleep(.2)
        if os.path.exists(screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]+".png"):
            print("Deleted Off",port)
            os.remove(screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]+".png")
    try:
        del active_threads[port]
    except:
        pass


def getOffInfoFromFolder(folderPath,port):
    offFullPath = os.path.join(folderPath,str(int(str(port)[-2:])),offFile)
    # print(offFullPath)
    if os.path.exists(offFullPath):
        return True#,offFullPath,os.path.getctime(offFullPath)
    else:
        return False#,None,None


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
        if os.path.exists(screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]+".png"):
            creation_time = datetime.fromtimestamp(os.path.getctime(screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]+".png"))
            current_time = datetime.now()
            age = current_time - creation_time
            if age > timedelta(minutes=2):
                print("Deleted Off",port)
                try:
                    del active_threads[port]
                    os.remove(screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]+".png")
                except:
                    sleep(.2)
                    try:
                        del active_threads[port]
                    except:
                        pass
                    if os.path.exists(screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]+".png"):
                        print("Deleted Off",port)
                        os.remove(screenshot_path+socket.gethostname().replace("-","")+"-"+str(port)[-3:]+".png")


# print(getOffInfoFromFolder(sharedFolderPath,5501))

while True:
    for i in range(30): #a cada 10s*6(1m)*10(10m)*6(60m) deletar as imagens
        for port in range(5001, 5301):#range(5510,5511):#
            
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
                if not isHostActive and getOffInfoFromFolder(sharedFolderPath,port):
                    deleteImages(host,port)
                    del active_threads[port]
                    print("deletadas",port)
        except:
            pass

        sleep(10)
