import os


def paketinstall():
    giris = input("Yüklenecek paket: ")
    os.system("sudo apt-get install "+giris)
    pass
def paketremove():
    giris = input("Silinecek paket: ")
    os.system("sudo apt-get remove "+giris)
    pass
def repo():
    os.system("cat /etc/apt/sources.list")
    pass
def repoedit():
    os.system("nano /etc/apt/sources.list")
    pass

