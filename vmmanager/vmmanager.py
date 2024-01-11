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

def createFile(fileName, content,folderPath):
        file_path = os.path.join(folderPath, fileName)

        # Create the folder if it doesn't exist
        file_path = os.path.join(folderPath, fileName)
        dirname = os.path.dirname(file_path)
        
        # Create the folder if it doesn't exist
        os.makedirs(dirname, exist_ok=True)
        try:
            with open(file_path, 'x') as file:
                file.write(content)
                return True
        except FileExistsError:
            print(f"File '{fileName}' already exists. Skipping creation.")
            return False


def createConfigFile(defaultSimulVms=defaultSimulVms,defaultSimulVmsString=defaultSimulVmsString):
    confFullPath = os.path.join(configPath,configFile)
    if os.path.exists(confFullPath) == False:
        createFile(configFile,f"""{defaultSimulVmsString}{str(defaultSimulVms)}""",configPath)
    else:
        print("arquvio existe")


def readLineContaining(fileName,targetString,folderPath):
        filePath = os.path.join(folderPath, fileName)
        with open(filePath, 'r') as file:
            lines = file.readlines()
        for line in lines:
            if targetString in line:
                return line


def readConfigFile():
    simulVms = int(readLineContaining(configFile,defaultSimulVmsString,configPath).replace(defaultSimulVmsString,""))
    return simulVms,None


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
            listOfOffInfos.append([os.path.dirname(fileInfo[1]),fileInfo[2]])
    return listOfOffInfos

def getCheckIfTurnOneOn(qtdConfig,sharedConfigFolders,listOfOffs):
    currentRunning = len(sharedConfigFolders)-len(listOfOffs)
    if currentRunning >= qtdConfig:
        return False
    else:
        return True
def getStatus(qtdConfig,sharedConfigFolders,listOfOffs):
    print("MaxSimulVms: ",qtdConfig)
    currentRunning = len(sharedConfigFolders)-len(listOfOffs)
    print("CurrOn: ",currentRunning,"CurrStandby: ",len(listOfOffs))
    # print(listOfOffs,sharedConfigFolders)
    allNumbers = []
    offNumbers = []
    for all in sharedConfigFolders:
        allNumbers.append(all.split("\\")[-1])
    for off in listOfOffs:
        offNumbers.append(off[0].split("\\")[-1])
    # print(allNumbers,offNumbers)
    print("CurrOnIds: ",list(set(allNumbers)-set(offNumbers)))
    

def getOldestOffFile(listOfOffs):
    oldestPath = listOfOffs[0][0]
    oldestTime = listOfOffs[0][1]
    for path,date in listOfOffs:
        if date < oldestTime:
            oldestTime = date
            oldestPath = path
    return oldestPath,oldestTime

def startVm(startPath):
    fullStartPath = os.path.join(startPath,startFile)
    fullOffPath = os.path.join(startPath,offFile)
    
    result = subprocess.run([fullStartPath], capture_output=True, text=True, check=True)
    print(datetime.datetime.now())
    print("Started Vm",startPath)
    if os.path.exists(fullOffPath):
        print("Deleted Off")
        os.remove(fullOffPath)

def removeREDOS(offs,timeFromOffInMinutes=10):
    threads = []
    for i in offs:
        hasBeenOffFor = datetime.datetime.now()-datetime.datetime.fromtimestamp(i[1])
        if hasBeenOffFor > datetime.timedelta(minutes=timeFromOffInMinutes):
            sleep(.01)
            folderNumber = i[0].split("\\")[-1]
            thread = threading.Thread(target=removeREDOSAction, args=(folderNumber,))
            threads.append(thread)
            thread.start()
            # removeREDOSAction(folderNumber)
            # print(folderNumber,hasBeenOffFor)

def removeREDOSAction(folderNumber):
    if not is_screen_active(int(folderNumber)+5000):
                VmFullPath = os.path.join(baseVirtualMachinesFolder,folderNumber)
                print(VmFullPath)
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

createConfigFile()
counter = 60
while True:
    counter +=1
    simulVms,*_ = readConfigFile()
    a = getSharedConfigFolders()
    offs = getListOfOffs(a)
    




    if counter >= timeBetweenStatusInMinutes*2:
        counter = 0
        print("Removing files with 'REDO' in the name:")
        removeREDOS(offs)
        print("The files have been Removed.")
        getStatus(simulVms,a,offs)
    if getCheckIfTurnOneOn(simulVms,a,offs):
        e,*_ = getOldestOffFile(offs)
        startVm(e)
        sleep(5)
        a = getSharedConfigFolders()
        offs = getListOfOffs(a)
        getStatus(simulVms,a,offs)
    for i in range(30):
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