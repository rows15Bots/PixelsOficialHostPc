from vncdotool import api
import threading
from time import sleep
import time
import socket
import os

def capture_screenshot(host="127.1.1.0",port=5505):
    connectTo = host+"::"+str(port)
    try:
        print("Getting screenshot of",port)

        client = api.connect(connectTo)
        sleep(1)
        # current_time = time.time()
        # sleep_duration = 2 - (current_time % 2)  # Adjust 2 to the desired even interval
        # sleep(sleep_duration)
        client.refreshScreen()
        client.captureScreen("test.png",True)
        # client.captureRegion("test.png",0,0,1920,1080,True)
        sleep(3)
        client.disconnect()
        print("OK",port)

        sleep(1)  # Wait for 3 seconds before refreshing the screenshot
    except:
        pass   

capture_screenshot(port=5502)