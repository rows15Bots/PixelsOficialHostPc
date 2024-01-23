import os
from subprocess import Popen
def actionTaker(action,vmRange):
        # Define the paths
        virtualMachinesFolder = r"C:\Virtual Machines"
        sharedFolder = r"C:\VmSharedFolder"
        match action:
            case "offs"|"aoff":
                print("this will create offs in the folders chosen if it doesn't already exists")
                for number in vmRange:
                    off_file_path = os.path.join(sharedFolder, str(number), 'off.txt')
                    if not os.path.exists(off_file_path):
                        try:
                            with open(off_file_path, 'w') as off_file:
                                off_file.write("off")
                            print("Created Off:",number)
                        except Exception as e:
                            print(e)

action = 'aoff'
vmRange = range(1,300)
actionTaker(action,vmRange)
os.chdir(r"C:\Pixels\vmmanager")
os.startfile("start filecleaner.bat")
os.startfile("start.bat")



# print(source_folder_path)
# print(destination_folder_path)