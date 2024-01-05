import os
import shutil
import fileinput
import sys
from time import sleep
import subprocess

# string1 = False
# string2 = False
# string3 = False
# string4 = False

# def checkCustomPaths():
#     pstring1 = r"C:\Program Files (x86)\VMware\VMware Workstation"
#     pstring2 = r"C:\Program Files (x86)\VMware\VMware Workstation"
#     pstring2 = r"C:\Program Files (x86)\VMware\VMware Workstation"
#     pstring2 = r"C:\Program Files (x86)\VMware\VMware Workstation"
#     pstring2 = r"C:\Program Files (x86)\VMware\VMware Workstation"
#     print(os.path.exists(pstring1))
# checkCustomPaths()

# configPath = r"C:\\PixelsConfig\\"
# configFile = r"pixelsVmHelperCreation.txt"
# defaultVmWareFolderString = "Vmware Folder: "
def interpretActionRange(actionRange):
    if ':' in actionRange:
        # If ':' is present, split and return number1, number2
        try:
            number1, number2 = map(int, actionRange.split(':'))
            return number1, number2
        except ValueError:
            print("Invalid range format. Please enter a valid range.")
            return None, None
    else:
        # If ':' is not present, return number1, number1
        try:
            number1 = int(actionRange)
            return number1, number1
        except ValueError:
            print("Invalid range format. Please enter a valid range.")
            return None, None
        
def inputGetter():
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    print("c    =  Create Vms")
    print("hnp  = Make Hdds Non Persistent")
    print("hp   = Make Hdds Persistent")
    print("mnem = Check for Mnems in Shared config")
    print("offs = Create offs in the folders selected")
    print("s    = Start Fresh Machines")
    # print("shut = Shutdown all machines")
    print("qqq  = Exits Script")

    action = input("Choose Action: ")
    if action not in ["c","hnp","hp","mnem","offs","s","qqq"]:
        print("Failed to interpret the Action.")
        return None,None
    if action == "qqq":
        sys.exit()

    actionRange = input("Choose VMs Range (e.g., '3:5' or '4'): ")
    print(actionRange)
            
    number1, number2 = interpretActionRange(actionRange)
    if number1 is not None and number2 is not None:
        # Create a range object
        vmRange = range(number1, number2 + 1)
        print(f"VM Action: {action}")
        print(f"VM Range: {list(vmRange)}")
        return action,vmRange
    else:
        print("Failed to interpret the VM range.")
        return None,None
    


def actionTaker(action,vmRange):
        # Define the paths
        virtualMachinesFolder = r"C:\Virtual Machines"
        sharedFolder = r"C:\VmSharedFolder"
        match action:
            case "offs":
                print("this will create offs in the folders chosen if it doesn't already exists")
                input("press Enter to continue...")
                for number in vmRange:
                    off_file_path = os.path.join(sharedFolder, str(number), 'off.txt')
                    if not os.path.exists(off_file_path):
                        with open(off_file_path, 'w') as off_file:
                            off_file.write("off")
                        print("Created Off:",number)


            case "mnem":
                print("this will check if the len is >12 characters long AND if it is empty")
                printString = input("print results (y/n):")
                wrongMnems = []
                correctMnems = []
                for number in vmRange:
                        sharedConfig_file_path = os.path.join(sharedFolder, str(number), 'sharedConfig.json')
                        if os.path.exists(sharedConfig_file_path):
                            with open(sharedConfig_file_path, 'r') as file:
                                for line in file:
                                    if '"mnem":' in line:
                                        if len(line.split(":")[1]) < 12 or '""' in line:
                                            wrongMnems.append([number,line])
                                        else:
                                            correctMnems.append(number)
                                        if printString == "y" or printString == "Y":
                                            print(line)
                for i in range(30):
                    print(" ")
                print("-------------------------")
                print("Wrong Mnems:")
                for i in wrongMnems:
                    print(i)
                print("Correct Mnems:")
                print(correctMnems)


            case "s":
                stillNeedsToStart = []
                print("Remember to add the vms to vmware to track progress")
                maxvms = input("Max Simult Vms: ")
                if not maxvms.isdigit():
                    print("Invalid input. Please enter a valid number.")
                    return
                maxvms = int(maxvms)
                started_vms = set()
                stillHasVmsToStart = True
                while stillHasVmsToStart == True:
                    print("--------------")
                    print(f'Max Vms: {len(started_vms.copy())}/{maxvms}')
                    print(f"Started Vms: {started_vms.copy()}")
                    print(f"Number of waiting to Start: {len(stillNeedsToStart)}")
                    print(f"Who still needs to start: {stillNeedsToStart}")
                    print("--------------")
                    ##Liga as vms
                    counter = 0
                    while len(started_vms) < maxvms and counter < 90:
                        counter +=1
                        for number in vmRange:
                            if not len(started_vms) < maxvms:
                                break
                            destination_folder_name = str(number)
                            fresh_vm_path = os.path.join(virtualMachinesFolder, destination_folder_name, 'freshVm.txt')
                            if os.path.exists(fresh_vm_path) and number not in started_vms:
                                print(os.path.exists(fresh_vm_path),fresh_vm_path)
                                # Run the VMX file
                                vmx_file_path = os.path.join(virtualMachinesFolder, destination_folder_name, f"{destination_folder_name}.vmx")
                                # cmdString = r'"C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmrun" start ' + f'"{vmx_file_path}"'
                                cmdString = r'"C:\Program Files (x86)\VMware\VMware Workstation\vmrun" start ' + f'"{vmx_file_path}"' + ' nogui'
                                print(cmdString)
                                subprocess.run(cmdString, shell=True)
                                # os.system(cmdString)
                                print(f"VMX file '{destination_folder_name}.vmx' started.")
                                started_vms.add(number)


                    sleep(1)
                    ##Checa as vms
                    for number in started_vms.copy():
                        off_file_path = os.path.join(sharedFolder, str(number), 'off.txt')
                        if os.path.exists(off_file_path):
                            started_vms.remove(number)
                            # Remove only the freshVm.txt
                            os.remove(os.path.join(virtualMachinesFolder, str(number), 'freshVm.txt'))
                    sleep(1)
                    #Checa os fresh.txt
                    stillHasVmsToStart = False
                    stillNeedsToStart = []
                    for number in vmRange:
                        destination_folder_name = str(number)
                        fresh_vm_path = os.path.join(virtualMachinesFolder, destination_folder_name, 'freshVm.txt')

                        if os.path.exists(fresh_vm_path):
                            stillHasVmsToStart = True
                            stillNeedsToStart.append(number)

                print("-------------------------------------")
                print("All Vms have been Started")
                print("-------------------------------------")


            case "hnp":
                for number in vmRange:
                    destination_folder_name = str(number)
                    new_vmx_file_path = os.path.join(virtualMachinesFolder, destination_folder_name, f"{destination_folder_name}.vmx")

                    # Add lines to the .vmx file
                    with open(new_vmx_file_path, 'a') as vmx_file:
                        vmx_file.write("nvme0:0.mode = \"independent-nonpersistent\"\n")

            case "hp":
                for number in vmRange:
                    destination_folder_name = str(number)
                    new_vmx_file_path = os.path.join(virtualMachinesFolder, destination_folder_name, f"{destination_folder_name}.vmx")

                    # Remove line from the .vmx file
                    with fileinput.FileInput(new_vmx_file_path, inplace=True) as vmx_file:
                        for line in vmx_file:
                            if 'nvme0:0.mode = "independent-nonpersistent"' not in line:
                                print(line, end='')
            case "c":
                source_folder_name = "change_me_n"
                for number in vmRange:
                    destination_folder_name = str(number)

                    # Construct full paths
                    source_folder_path = os.path.join(virtualMachinesFolder, source_folder_name)
                    destination_folder_path = os.path.join(virtualMachinesFolder, destination_folder_name)

                    if os.path.exists(destination_folder_path):
                        print(f"Dest folder '{destination_folder_path}' already exists. Skipping.")
                    else:
                        if not os.path.exists(source_folder_path):
                            print(f"Source folder '{source_folder_name}' not found.")

                        else:
                            # Copy the folder
                            shutil.copytree(source_folder_path, destination_folder_path)   
                            # Rename the .vmx file
                            vmx_file_path = os.path.join(destination_folder_path, f"{source_folder_name}.vmx")
                            new_vmx_file_path = os.path.join(destination_folder_path, f"{destination_folder_name}.vmx")
                            os.rename(vmx_file_path, new_vmx_file_path)

                            print(f"Folder '{source_folder_name}' copied and renamed to '{destination_folder_name}'.")
                            print(f".vmx file renamed to '{destination_folder_name}.vmx'.") 

                            # Create 'freshVm.txt' inside the destination folder
                            fresh_vm_txt_path = os.path.join(destination_folder_path, 'freshVm.txt')
                            with open(fresh_vm_txt_path, 'w') as fresh_vm_file:
                                fresh_vm_file.write("This is a fresh VM.")

                            # Modify specific lines in the .vmx file
                            with fileinput.FileInput(new_vmx_file_path, inplace=True) as vmx_file:
                                for line in vmx_file:
                                    line = line.replace(f'displayName = "change_me_n"', f'displayName = "{destination_folder_name}"')
                                    line = line.replace(f'guestinfo.botId = "change_me_n"', f'guestinfo.botId = "{destination_folder_name}"')
                                    line = line.replace(f'RemoteDisplay.vnc.port = "change_me_vnc"', f'RemoteDisplay.vnc.port = "{int(destination_folder_name) + 5000}"')
                                    print(line, end='')

while True:
    action = None
    vmRange = None
    action,vmRange = inputGetter()
    if action != None and vmRange != None:
        actionTaker(action,vmRange)



# print(source_folder_path)
# print(destination_folder_path)