from logTest import logging,rowsLog


logLevel = "DEBUG"  # Set the desired log level for the entire file
match logLevel: 
    case "DEBUG": logLevel = logging.DEBUG
    case "WARNING": logLevel = logging.WARNING
    case "INFO": logLevel = logging.INFO
    case "ERROR": logLevel = logging.ERROR


@rowsLog(log_level=logLevel)
def rows():
    return 1+2
@rowsLog(log_level=logLevel,alwaysLog=True,dev=True)
def rows2(a=3):
    return 1+2+a


print(rows(),rows2(2))






























# from vncdotool import api
# import threading
# from time import sleep
# import time
# import socket
# import os
# import logging
# from icecream import ic, IceCreamDebugger
# import ycecream
# logLevel = "INFO"
# logging.basicConfig(level=logLevel)
# log = logging.getLogger(__name__)
# match logLevel:
#     case "DEBUG":
#         yc = ycecream.y.configure(output=log.debug,prefix=" ",show_enter=True,show_exit=True)
#     case "INFO":
#         yc = ycecream.y.configure(output=log.info,prefix=" ",show_enter=True,show_exit=False)


# # yc= ycecream.y.configure(output=log.debug,prefix="Debug => ",show_enter=False,show_exit=True)
# # yc.configure(show_delta=False,show_time=False,compact=True,line_length=3,wrap_indent=20,values_only=True,values_only_for_fstrings=True)
# # print(ycInfo is ycDbg)
# # print(ycDbg.configure())
# class Palhaco():
#     # @ycInfo()
#     @yc()
#     def apertarNariz(self):
#         pass
        
#         # print("honk!")
#     @yc()
#     def levantarDedos(self,quantidade):
#         # print(vars())
#         pass
#         # print(f"levantei {quantidade} dedos")
#     @yc()
#     def somarSalarioMentalmente(self,dia1,dia2,dia3):
#         return sum([dia1,dia2,dia3])
    
# p = Palhaco()

# p.apertarNariz()
# p.levantarDedos(3)
# p.somarSalarioMentalmente(3,5,2)