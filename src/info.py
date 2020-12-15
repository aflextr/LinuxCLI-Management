import platform
import os
import sys

def dist():
    a = platform.dist()
    print("Dağıtım:"+a[0]+":"+a[1])
    pass
def kernel():
    print("Kernel sürümünüz : "+platform.release())
    pass
def time():
    os.system("date")
def cpu():
    os.system("cat /proc/cpuinfo")
    pass
def ram():
        os.system("free -h")
        pass