import os
import sys
from time import sleep
from pathlib import Path
import subprocess
import datetime
import threading

#FUTURO ler data da sauna vip e botar no começo da fila

#Static Info:

ipfile = r"ip.txt"
approved = "approved"
rejected = "rejected"
asking = "asking"
sharedConfigFolders =   ["\\\\DESKTOP-CCBHJE3\\VmSharedFolder",
                         "\\\\DESKTOP-A804AU5\\VmSharedFolder",
                         "\\\\RIG001\\VmSharedFolder",
                         "\\\\RIG002\\VmSharedFolder",
                         "\\\\RIG003\\VmSharedFolder",
                         "\\\\SVI7\\VmSharedFolder",
                         "\\\\SVXEON\\VmSharedFolder",
                        #  "\\\\ZPANGA\\VmSharedFolder"
                        ]

defaultSimulVmsString = "Status: "

autoRejectIps = []

approvedIps = []

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

            



lock = threading.Lock()

def get_approved_ips(folder, folder_number,readableOutput=False):
    folder_path = os.path.join(folder, str(folder_number))
    ip_txt_path = os.path.join(folder_path, "ip.txt")

    if os.path.exists(ip_txt_path):
        try:
            status = readLineContaining(ip_txt_path,"Status: ","").replace("Status: ","").replace("\n","")
        except Exception as e:
            print(f"An exception occurred: {e}")
            with open(ip_txt_path, 'w') as file:
                file.write('Ip: off\nStatus: rejected')
            sleep(1)
            status = readLineContaining(ip_txt_path,"Status: ","").replace("Status: ","").replace("\n","")
        if approved in status:
            # print(status)
            ip = readLineContaining(ip_txt_path,"Ip: ","").replace("Ip: ","").replace("\n","")
            # print(ip)
            with lock:
                if readableOutput == True:
                    if ip in approvedIps and ip != "off":
                        print(folder.replace("\\","").replace("VmSharedFolder","")+" "+str(folder_number)+" - "+ip)
                else:
                    if ip not in approvedIps:
                        approvedIps.append(ip)

def set_status_ips(folder, folder_number):
    folder_path = os.path.join(folder, str(folder_number))
    ip_txt_path = os.path.join(folder_path, "ip.txt")

    if os.path.exists(ip_txt_path):
        try:
            status = readLineContaining(ip_txt_path,"Status: ","").replace("Status: ","").replace("\n","")
        except Exception as e:
            print(f"An exception occurred: {e}")
            with open(ip_txt_path, 'w') as file:
                file.write('Ip: off\nStatus: rejected')
            sleep(1)
            status = readLineContaining(ip_txt_path,"Status: ","").replace("Status: ","").replace("\n","")
        if asking in status:
            # print(status)
            # print(status)
            ip = readLineContaining(ip_txt_path,"Ip: ","").replace("Ip: ","").replace("\n","")
            with lock:
                print(" ")
                if ip not in approvedIps:
                    print("Action: ",approved,folder.replace("\\","").replace("VmSharedFolder","")+" "+str(folder_number)+" - "+ip)
                    editLineContaining(ip_txt_path,"Status: ","Status: "+approved,"")
                else:
                    print("Action: ",rejected,folder.replace("\\","").replace("VmSharedFolder","")+" "+str(folder_number)+" - "+ip)
                    editLineContaining(ip_txt_path,"Status: ","Status: "+rejected,"")

# Function to create and start threads for a shared folder
def create_and_start_threads_ids(shared_folder,readOrWrite):
    
    # match readOrWrite:
        if readOrWrite ==  'read':
            threads = []
            for i in range(1, 301):
                thread = threading.Thread(target=get_approved_ips, args=(shared_folder, i))
                threads.append(thread)
                thread.start()

            # Wait for all threads to finish
            for thread in threads:
                thread.join()
        if readOrWrite ==  'write':
            threads = []
            for i in range(1, 301):
                thread = threading.Thread(target=set_status_ips, args=(shared_folder, i))
                threads.append(thread)
                thread.start()

            # Wait for all threads to finish
            for thread in threads:
                thread.join()
        if readOrWrite ==  'status':
            threads = []
            for i in range(1, 301):
                thread = threading.Thread(target=get_approved_ips, args=(shared_folder, i, True))
                threads.append(thread)
                thread.start()

            # Wait for all threads to finish
            for thread in threads:
                thread.join()

# Create and start threads for each shared folder
def create_and_start_threads_folders(readOrWrite):
    # match readOrWrite:
        if readOrWrite == 'read':
            shared_folder_threads = []
            for shared_folder in sharedConfigFolders:
                thread = threading.Thread(target=create_and_start_threads_ids, args=(shared_folder,'read',))
                shared_folder_threads.append(thread)
                thread.start()

            # Wait for all shared folder threads to finish
            for thread in shared_folder_threads:
                thread.join()
        if readOrWrite ==  'write':
            shared_folder_threads = []
            for shared_folder in sharedConfigFolders:
                thread = threading.Thread(target=create_and_start_threads_ids, args=(shared_folder,'write',))
                shared_folder_threads.append(thread)
                thread.start()

            # Wait for all shared folder threads to finish
            for thread in shared_folder_threads:
                thread.join()

        if readOrWrite ==  'status':
            shared_folder_threads = []
            for shared_folder in sharedConfigFolders:
                thread = threading.Thread(target=create_and_start_threads_ids, args=(shared_folder,'status',))
                shared_folder_threads.append(thread)
                thread.start()

            # Wait for all shared folder threads to finish
            for thread in shared_folder_threads:
                thread.join()

# sleep(1)  
counter = 26
while True:
    counter +=1
    #Default Reject:
    approvedIps = [
        "179.111.62.59", #my ip

        # "154.6.130.149", #bad ips
        "178.175.129.44",
        "191.101.210.141",
        "196.196.53.141",
        "196.196.53.137",
        "196.196.53.135",
        "45.133.193.45",


        ]
    create_and_start_threads_folders('read')
    sleep(1)
    create_and_start_threads_folders('write')
    
    if counter %27 == 0:
        print(" ")
        create_and_start_threads_folders('status')
        print(" ")
    print("-")#, end ="")
    sleep(1)


    # print("read Ips:")
    # approvedIps.sort()
    # for i in approvedIps:
    #     print(i)










# def getAskingOffFiles():
# for number in vmRange:
#                     destination_folder_name = str(number)
#                     new_vmx_file_path = os.path.join(virtualMachinesFolder, destination_folder_name, f"{destination_folder_name}.vmx")




# def getSharedConfigFolders(p = None):
    
    
#     p = Path(p)
#     sharedConfigFolderFileList = list(p.glob("./*/sharedConfig.json"))
#     sharedConfigFolderList = []
#     for folder in sharedConfigFolderFileList:
#         sharedConfigFolderList.append(os.path.dirname(folder))
#     return sharedConfigFolderList

# def getListOfIpFiles(sharedConfigFolders):
#     listOfIpFiles = []
#     for folder in sharedConfigFolders:
#         fileInfo = getIpFileFromFolder(folder)
#         if fileInfo[0]:
#             listOfIpFiles.append(fileInfo[1])
#     return listOfIpFiles

# def getIpFileFromFolder(folderPath):
#     ipFullPath = os.path.join(folderPath,ipfile)
#     if os.path.exists(ipFullPath):
#         return [True,ipFullPath]
#     else:
#         return [None,None]
#     ###
# def editLineContaining(fileName, targetString, newContent,folderPath = None):

#         filePath = os.path.join(folderPath, fileName)
#         try:
#             with open(filePath, 'r') as file:
#                 lines = file.readlines()

#             editedLines = [newContent+"\n" if targetString in line else line for line in lines]

#             with open(filePath, 'w') as file:
#                 file.writelines(editedLines)
#         except FileNotFoundError:
#             print(f"File '{fileName}' not found.")


# currIpList = []

# def ipManagerAdd(sharedFolderName):
#     #Get ip files and list them
#     listOfIpFiles = getListOfIpFiles(getSharedConfigFolders(sharedFolderName))
#     #Get Ips and save in a list
#     for file in listOfIpFiles:
#         ip = readLineContaining(file,"Ip: ","").replace("Ip: ","").replace("\n","")
#         status = readLineContaining(file,"Status: ","").replace("Status: ","").replace("\n","")
#         # print("FileStatus",ip,status)
#         if ip not in currIpList and asking not in status:
#             currIpList.append(ip)

# def ipManagerAnswer(sharedFolderName):
#     listOfIpFiles = getListOfIpFiles(getSharedConfigFolders(sharedFolderName))
#     for file in listOfIpFiles:
#         ip = readLineContaining(file,"Ip: ","").replace("Ip: ","").replace("\n","")
#         status = readLineContaining(file,"Status: ","").replace("Status: ","").replace("\n","")
#         if asking in status:
#             if ip not in currIpList:
#                 currIpList.append(ip)
#                 #editfile to approved
#                 print("Action: ",approved,ip,file)
#                 editLineContaining(file,"Status: ","Status: "+approved,"")
#             else:
#                 print("Action: ",rejected,ip,file)
#                 editLineContaining(file,"Status: ","Status: "+rejected,"")
#         # if rejected in status or approved in status:
#         #     editLineContaining(file,"Status: ","Status: "+asking,"")
#         #     print("Resetando",file)
# counter = 4    
# while True:
#     counter +=1
#     print("-----------")
#     currIpList = []
#     for f in sharedConfigFolders:
#         print(f)
#         try:
#             if os.path.exists(f):
#                 ipManagerAdd(f)
#             else:
#                 print(f,"not available")
#         except Exception as e:
#             print(e)
#     print("-------------------JDDJDJJD")
#     for f in sharedConfigFolders:
#         try:
#             if os.path.exists(f):
#                 ipManagerAnswer(f)
#             else:
#                 print(f,"not available")
#         except Exception as e:
#             print(e)
#     if counter %5 == 0:
#         print(currIpList)
#     sleep(1)
# #Check for asking and add to the list if needed
#     # if asking in statusLine:
#     #     pass























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




