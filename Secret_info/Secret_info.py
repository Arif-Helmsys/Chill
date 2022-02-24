import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time
import requests
from bs4 import BeautifulSoup
import socket
import platform


__AUTHOR__ = "Helmsys"
class User:
    def __init__(self, email):
        self.email = email

        self.mail = smtplib.SMTP("smtp.gmail.com",587)          
        self.mail.ehlo()
        self.mail.starttls()
        self.mail.login("e-posta@gmail.com", "eposta_şifresi")

        self.mesaj = MIMEMultipart()
        self.image = MIMEImage(self.sendImage(r"D:\Bilgiler\logo.png"))
        self.mesaj["From"] = "e-posta@gmail.com"
        self.mesaj["To"] = self.email
        url_ip = "https://www.ipsorgu.com/"
        r = requests.get(url=url_ip)
        soup = BeautifulSoup(r.content,"lxml")
        self.ip = soup.find("span",attrs={"class":"ipadresiniz"}).text
        self.send_mail()

    def sendImage(self,img:str):
        with open(img,"rb") as f:
            self.data = f.read()
        return self.data
    
    def connect(self):
        __URL__ = f"http://ip-api.com/json/?fields=61439"
        r = requests.get(url=__URL__)
        self.json = r.json()
    
    def send_mail(self):
        self.connect()
        self.mesaj["Subject"] = "Bilgilerin"
        self.body = f"""
:------Cihazının Bilgileri------:
Bilgisayar Adın: {platform.node()} | İşletim Sistemin: {platform.platform()}
IP Adresin: {self.json["query"]} | IPv4 Adresin: {socket.gethostbyname(socket.gethostname())}
İnternet Sağlayıcın (ISP): {self.json["isp"]}

:------Tahmini Konum Bilgilerin------:
Ülke: {self.json["country"]} | İl: {self.json["city"]}
Enlem: {self.json["lat"]} | Boylam: {self.json["lon"]}
\nHiçbir bilgi Geliştirici ile paylaşılmamıştır.
\n\nDeveloper by Helmsys™
"""
        self.body_text = MIMEText(self.body, "plain")  
        self.mesaj.attach(self.body_text)
        self.mesaj.attach(self.image)
        self.mail.sendmail( self.mesaj["From"], self.mesaj["To"], self.mesaj.as_string())
        time.sleep(3)
if __name__ =="__main__":
    print(f""" _______  _______  _______  _______  _______ _________  _________ _        _______  _______ 
(  ____ \(  ____ \(  ____ \(  ____ )(  ____ \\__   __/  \__   __/( (    /|(  ____ \(  ___  )
| (    \/| (    \/| (    \/| (    )|| (    \/   ) (        ) (   |  \  ( || (    \/| (   ) |
| (_____ | (__    | |      | (____)|| (__       | |        | |   |   \ | || (__    | |   | |
(_____  )|  __)   | |      |     __)|  __)      | |        | |   | (\ \) ||  __)   | |   | |
      ) || (      | |      | (\ (   | (         | |        | |   | | \   || (      | |   | |
/\____) || (____/\| (____/\| ) \ \__| (____/\   | |     ___) (___| )  \  || )      | (___) |
\_______)(_______/(_______/|/   \__/(_______/   )_(_____\_______/|/    )_)|/       (_______)
                               ({__AUTHOR__}™)  \n\n\n""")

    ask = input("Gizli bilgilerin E-posta ile bilgilendirilecek kabul ediyor musun? (e/h): ")
    if ask == "e":
        try:
            posta = input("E-Postanı gir: ")
            print("Bilgilerin E-Postana Yollanıyor...")
            User(posta)
            time.sleep(5)
            print(f'İLGİLİ BİLGİLER {posta} İLGİLİ E-POSTAYA GÖNDERİLDİ.')
            time.sleep(3)
            print("Çıkış Yapılıyor...")
        except smtplib.SMTPRecipientsRefused:
            print("Yazdığın e-postada hata var düzeltmek için programı yeniden başlat.")
            time.sleep(3)
    elif ask == "h":
        print("İptal Edildi\nÇıkış Yapılıyor")
        time.sleep(3)
        exit(0)
