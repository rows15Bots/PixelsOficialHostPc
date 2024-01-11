import os
import sys
from time import sleep
from pathlib import Path
import subprocess
import datetime
import socket
import threading
#FUTURO ler data da sauna vip e botar no começo da fila

#Static Info:

configPath = r"C:\\PixelsConfig\\"
configFile = r"pixelsVmManager.txt"
offFile = r"off.txt"
startFile = r"start.bat"
baseSharedConfigFolder = r"C:\\VmSharedFolder\\"
baseVirtualMachinesFolder = r"C:\\Virtual Machines\\"
defaultSimulVmsString = "Simultaneous Vms: "
defaultSimulVms = 1
timeBetweenStatusInMinutes = 3


#Functions

def getSharedConfigFolders():
    p = Path(baseSharedConfigFolder)
    sharedConfigFolderFileList = list(p.glob("./*/sharedConfig.json"))
    sharedConfigFolderList = []
    for folder in sharedConfigFolderFileList:
        testForNumbersSplit = str(os.path.dirname(folder)).split("\\")[-1]
        # print(testForNumbersSplit,testForNumbersSplit.isdigit())
        if testForNumbersSplit.isdigit():
            sharedConfigFolderList.append(os.path.dirname(folder))
    return sharedConfigFolderList

def getOffInfoFromFolder(folderPath):
    offFullPath = os.path.join(folderPath,offFile)
    if os.path.exists(offFullPath):
        return True,offFullPath,os.path.getctime(offFullPath)
    else:
        return False,None,None
    
def getListOfOffs(sharedConfigFolders):
    listOfOffInfos = []
    for file in sharedConfigFolders:
        fileInfo = getOffInfoFromFolder(file)
        if fileInfo[0]:
            # listOfOffInfos.append([os.path.dirname(fileInfo[1]),fileInfo[2]])
            hasBeenOffFor = datetime.datetime.now()-datetime.datetime.fromtimestamp(fileInfo[2])
            if hasBeenOffFor > datetime.timedelta(minutes=10):
                sleep(.1)
                folderNumber = os.path.dirname(fileInfo[1]).split("\\")[-1]
                print(folderNumber,"      Off for :", hasBeenOffFor.total_seconds()/60/60, " hours")
                removeREDOSAction(folderNumber)
    return listOfOffInfos


# def removeREDOS(offs,timeFromOffInMinutes=10):
#     for i in offs:
#         hasBeenOffFor = datetime.datetime.now()-datetime.datetime.fromtimestamp(i[1])
#         if hasBeenOffFor > datetime.timedelta(minutes=timeFromOffInMinutes):
#             sleep(.1)
#             folderNumber = i[0].split("\\")[-1]
#             print(folderNumber,hasBeenOffFor)
#             removeREDOSAction(folderNumber)

def removeREDOSAction(folderNumber):
    if not is_screen_active(int(folderNumber)+5000,timeout=3):
        if not is_screen_active(int(folderNumber)+5000,timeout=3):
            if not is_screen_active(int(folderNumber)+5000,timeout=3):
                VmFullPath = os.path.join(baseVirtualMachinesFolder,folderNumber)
                # print(VmFullPath)
                if os.path.isdir(VmFullPath):
                    redo_files = [file for file in os.listdir(VmFullPath) if 'REDO' in file and not 'lck' in file]
                    # print(redo_files)
                    if redo_files:
                        for redo_file in redo_files:
                            # print(os.path.join(VmFullPath, redo_file))
                            file_path = os.path.join(VmFullPath, redo_file)
                            try:
                                os.remove(file_path)
                                print(f"Deleted: {file_path}")
                            except Exception as e:
                                print(e)
                                pass
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



while True:

    a = getSharedConfigFolders()
    




    print("Removing files with 'REDO' in the name:")
    getListOfOffs(a)
    # removeREDOS(offs)
    print("The files have been Removed.")

    for i in range(10):
        sleep(1)





# createConfigFile()
# a = getSharedConfigFolders()
# # print(a)
# # print(b)
# c = getListOfOffs(a)
# # print(c)
# d = getCheckIfTurnOneOn(defaultSimulVms,a,c)
# # print(d)
# e,_ = getOldestOffFile(c)
# # print(e)
# print(startVm(e))