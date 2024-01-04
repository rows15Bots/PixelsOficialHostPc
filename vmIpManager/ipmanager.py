import os
import sys
from time import sleep
from pathlib import Path
import subprocess
import datetime


#FUTURO ler data da sauna vip e botar no começo da fila

#Static Info:

ipfile = r"ip.txt"
approved = "approved"
rejected = "rejected"
asking = "asking"
baseSharedConfigFolder = r"C:\\VmSharedFolder\\"
sharedConfigFolders =   ["\\\\DESKTOP-CCBHJE3\\VmSharedFolder",
                         "\\\\DESKTOP-A804AU5\\VmSharedFolder",
                         "\\\\ZPANGA\\VmSharedFolder"]

defaultSimulVmsString = "Status: "



#Functions


def readLineContaining(fileName,targetString,folderPath):
        filePath = os.path.join(folderPath, fileName)
        try:
            with open(filePath, 'r') as file:
                lines = file.readlines()
            for line in lines:
                if targetString in line:
                    return line
        except:
            sleep(.1)
            try:
                with open(filePath, 'r') as file:
                    lines = file.readlines()
                for line in lines:
                    if targetString in line:
                        return line
            except:
                pass


def getSharedConfigFolders(p = None):
    if p == None:
        p = Path(baseSharedConfigFolder)
    else:
        p = Path(p)
    sharedConfigFolderFileList = list(p.glob("./*/sharedConfig.json"))
    sharedConfigFolderList = []
    for folder in sharedConfigFolderFileList:
        sharedConfigFolderList.append(os.path.dirname(folder))
    return sharedConfigFolderList

def getListOfIpFiles(sharedConfigFolders):
    listOfIpFiles = []
    for folder in sharedConfigFolders:
        fileInfo = getIpFileFromFolder(folder)
        if fileInfo[0]:
            listOfIpFiles.append(fileInfo[1])
    return listOfIpFiles

def getIpFileFromFolder(folderPath):
    ipFullPath = os.path.join(folderPath,ipfile)
    if os.path.exists(ipFullPath):
        return [True,ipFullPath]
    else:
        return [None,None]
    ###
def editLineContaining(fileName, targetString, newContent,folderPath = None):

        filePath = os.path.join(folderPath, fileName)
        try:
            with open(filePath, 'r') as file:
                lines = file.readlines()

            editedLines = [newContent+"\n" if targetString in line else line for line in lines]

            with open(filePath, 'w') as file:
                file.writelines(editedLines)
        except FileNotFoundError:
            print(f"File '{fileName}' not found.")


currIpList = []

def ipManagerAdd(sharedFolderName):
    #Get ip files and list them
    listOfIpFiles = getListOfIpFiles(getSharedConfigFolders(sharedFolderName))
    #Get Ips and save in a list
    for file in listOfIpFiles:
        ip = readLineContaining(file,"Ip: ","").replace("Ip: ","").replace("\n","")
        status = readLineContaining(file,"Status: ","").replace("Status: ","").replace("\n","")
        # print("FileStatus",ip,status)
        if ip not in currIpList and asking not in status:
            currIpList.append(ip)

def ipManagerAnswer(sharedFolderName):
    listOfIpFiles = getListOfIpFiles(getSharedConfigFolders(sharedFolderName))
    for file in listOfIpFiles:
        ip = readLineContaining(file,"Ip: ","").replace("Ip: ","").replace("\n","")
        status = readLineContaining(file,"Status: ","").replace("Status: ","").replace("\n","")
        if asking in status:
            if ip not in currIpList:
                currIpList.append(ip)
                #editfile to approved
                print("Action: ",approved,ip,file)
                editLineContaining(file,"Status: ","Status: "+approved,"")
            else:
                print("Action: ",rejected,ip,file)
                editLineContaining(file,"Status: ","Status: "+rejected,"")
        # if rejected in status or approved in status:
        #     editLineContaining(file,"Status: ","Status: "+asking,"")
        #     print("Resetando",file)
counter = 4    
while True:
    counter +=1
    print("-----------")
    currIpList = []
    for f in sharedConfigFolders:
        if os.path.exists(f):
            ipManagerAdd(f)
        else:
            print(f,"not available")
    for f in sharedConfigFolders:
        if os.path.exists(f):
            ipManagerAnswer(f)
        else:
            print(f,"not available")
    if counter %5 == 0:
        print(currIpList)
    sleep(5)
#Check for asking and add to the list if needed
    # if asking in statusLine:
    #     pass























# def getCheckIfTurnOneOn(qtdConfig,sharedConfigFolders,listOfOffs):
#     currentRunning = len(sharedConfigFolders)-len(listOfOffs)
#     if currentRunning >= qtdConfig:
#         return False
#     else:
#         return True
# def getStatus(qtdConfig,sharedConfigFolders,listOfOffs):
#     print("MaxSimulVms: ",qtdConfig)
#     currentRunning = len(sharedConfigFolders)-len(listOfOffs)
#     print("CurrOn: ",currentRunning,"CurrStandby: ",len(listOfOffs))
#     # print(listOfOffs,sharedConfigFolders)
#     allNumbers = []
#     offNumbers = []
#     for all in sharedConfigFolders:
#         allNumbers.append(all.split("\\")[-1])
#     for off in listOfOffs:
#         offNumbers.append(off[0].split("\\")[-1])
#     # print(allNumbers,offNumbers)
#     print("CurrOnIds: ",list(set(allNumbers)-set(offNumbers)))
    

# def getOldestOffFile(listOfOffs):
#     oldestPath = listOfOffs[0][0]
#     oldestTime = listOfOffs[0][1]
#     for path,date in listOfOffs:
#         if date < oldestTime:
#             oldestTime = date
#             oldestPath = path
#     return oldestPath,oldestTime

# def startVm(startPath):
#     fullStartPath = os.path.join(startPath,startFile)
#     fullOffPath = os.path.join(startPath,offFile)
    
#     result = subprocess.run([fullStartPath], capture_output=True, text=True, check=True)
#     print(datetime.datetime.now())
#     print("Started Vm",startPath)
#     if os.path.exists(fullOffPath):
#         print("Deleted Off")
#         os.remove(fullOffPath)
    


# #Main

# createConfigFile()
# counter = 60
# while True:
#     counter +=1
#     simulVms,*_ = readConfigFile()
#     a = getSharedConfigFolders()
#     offs = getListOfOffs(a)
#     if counter >= timeBetweenStatusInMinutes*2:
#         counter = 0
#         getStatus(simulVms,a,offs)
#     if getCheckIfTurnOneOn(simulVms,a,offs):
#         e,*_ = getOldestOffFile(offs)
#         startVm(e)
#         sleep(5)
#         a = getSharedConfigFolders()
#         offs = getListOfOffs(a)
#         getStatus(simulVms,a,offs)
#     for i in range(30):
#         sleep(1)




