from src import info
from src import network
from src import paket
from src import update
import time


def motd():
    print("******************************************")
    print("******************************************")
    print("******************************************")
    print("****************Linux CLİ*****************")
    print("******************************************")
    print("******************************************")
    print("******************************************\n\n")
    pass

def main():
    motd()
    print("1-SİSTEM BİLGİSİ İÇİN")
    print("2-PAKET YÖNETİCİSİ İÇİN")
    print("3-AĞ YÖNETİMİ İÇİN")
    print("4-PROGRAMI GÜNCELLEMEK İÇİN")
    print("5-Çıkış\n\n")
    giris = int(input(":"))
    if giris == 1:
        def sistem():
            motd()
            print("1-DAĞITIM BİLGİSİ İÇİN")
            print("2-KERNEL BİLGİSİ İÇİN")
            print("3-ZAMAN BİLGİSİ İÇİN")
            print("4-CPU BİLGİSİ İÇİN")
            print("5-RAM BİLGİSİ İÇİN")
            print("6-GERİ")
            giris1 = int(input(":"))
            if giris1 == 1:
                info.dist()
                time.sleep(3)
                sistem()
                pass
            elif giris1 == 2:
                info.kernel()
                time.sleep(3)
                sistem()
                pass
            elif giris1 == 3:
                info.time()
                time.sleep(3)
                sistem()
                pass
            elif giris1 == 4:
                info.cpu()
                time.sleep(3)
                sistem()
                pass
            elif giris1 == 5:
                info.ram()
                time.sleep(3)
                sistem()
                pass
            elif giris1 == 6:
                main()
                pass
            pass
        sistem()
        
        pass
    elif giris == 2:
        def pakets():
            motd()
            print("1-PAKET YÜKLEMEK İÇİN")
            print("2-PAKET SİLMEK İÇİN")
            print("3-REPO BİLGİSİ İÇİN")
            print("4-REPO DÜZENLEMEK İÇİN")
            print("5-GERİ")
            giris2 = int(input(":"))
            if giris2 == 1:
                paket.paketinstall()
                time.sleep(3)
                pakets()
                pass
            elif giris2 == 2:
                paket.paketremove()
                time.sleep(3)
                pakets()
                pass
            elif giris2 == 3:
                paket.repo()
                time.sleep(3)
                pakets()
                pass
            elif giris2 == 4:
                paket.repoedit()
                time.sleep(3)
                pakets()
                pass
            elif giris2 == 5:
                main()
                time.sleep(1)
                pass
            pass
        pakets()
        
    
    elif giris == 3:
        def ag():
            motd()
            print("1-AĞ BİRİM BİLGİSİ İÇİN")
            print("2-PUBLİC İP İÇİN")
            print("3-PORT YÖNLENDİRME PROGRAMI İÇİN İÇİN")
            print("4-İP HARİTA İÇİN")
            print("5-GERİ")
            giris3 = int(input(":"))
            if giris3 == 1:
                network.ifconfig()
                time.sleep(3)
                ag()
                pass
            elif giris3 == 2:
                network.publicip()
                time.sleep(3)
                ag()
                pass
            elif giris3 == 3:
                network.ngrok()
                time.sleep(3)
                ag()
                pass
            elif giris3 == 4:
                network.ipmap()
                time.sleep(3)
                ag()
                pass
            elif giris3 == 5:
                main()
                time.sleep(1)
                pass
            pass
        ag()
        pass
    elif giris == 4:
        print("YAKINDA")
        time.sleep(1)
        main()
        pass
    elif giris == 5:
        exit
        pass
        


main()