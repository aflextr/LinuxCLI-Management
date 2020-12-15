import os
import sys
import requests
from bs4 import BeautifulSoup


def ifconfig():
    os.system("ifconfig")
    pass
def publicip():
    os.system("curl ifconfig.co")
    pass
def ngrok():
    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
    os.system("unzip ngrok-stable-linux-amd64.zip")
    giris = input("Ngrok authtoken :")
    os.system("./ngrok authtoken "+giris)
    os.system("rm -r ngrok-stable-linux-amd64.zip")
    pass
def ipmap():
    r = requests.get("https://www.infosniper.net/")
    Soup = BeautifulSoup(r.content,"html.parser")
    find = Soup.find(id="content")
    print(find.text)
    print("More: https://www.infosniper.net/")
    pass

