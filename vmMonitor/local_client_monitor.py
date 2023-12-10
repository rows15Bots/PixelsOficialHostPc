import os
import sys
from time import sleep
from pathlib import Path
import subprocess
import datetime


configPath = r"C:\\PixelsConfig\\"
configFile = r"pixelsVmManager.txt"
offFile = r"off.txt"
startFile = r"start.bat"
baseSharedConfigFolder = r"C:\\VmSharedFolder\\"
defaultSimulVmsString = "Simultaneous Vms: "
defaultSimulVms = 1
timeBetweenStatusInMinutes = 3