from glob import glob
import wget
from selenium import webdriver
import selenium
import time


PURPLE    = '\033[95m'
CYAN      = '\033[96m'
DARKCYAN  = '\033[36m'
BLUE      = '\033[94m'
GREEN     = '\033[92m'
YELLOW    = '\033[93m'
RED       = '\033[91m'
BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
END       = '\033[0m'

reset     = END

program_name = f"""{CYAN}{BOLD}
                                coding by
 _____ _______  ___ __                           __          __   
| _   |   _   .'  _|__.-----.-----.-----.----.  |  |--.-----|  |_ 
|.|   |.  |   |   _|  |     |  _  |  -__|   _|  |  _  |  _  |   _|
`-|.  |.  |   |__| |__|__|__|___  |_____|_______|_____|_____|____|
  |:  |:  |   |             |_____|       |______|                
  |::.|::.. . |                                   
  `---`-------'                 Helmsys
{reset}"""
class TenFingerBot:
    def __init__(self,url1,url2):
        self.url_chrome = url1
        self.url_edge = url2
        self.q = input(f"[{RED}+{RED}{reset}] {DARKCYAN}Hangi Tarayıcıyı kullanıyorsun {RED}>>> {PURPLE}")
        if self.q == "1":
            self.chrome()
        elif self.q == "2":
            self.edge()

    def chrome(self):
        if glob("chromedriver.exe"):
            print(f"\n{DARKCYAN}Chrome Driver'i yüklü. İşlem başlıyor....\n")
            time.sleep(2)
            print(f"Browser Açılıyor{reset}")
            time.sleep(1)
            self.system()
        else:
            print(f"\n{reset}[{RED}!{reset}] {DARKCYAN}Driver Yüklü değil{reset}\n")
            print(f"\t{reset}[{RED}-{reset}] {DARKCYAN}İndirme İşlemi Başlıyor{PURPLE}")
            time.sleep(3)
            print(f"{DARKCYAN}İndiriliyor...{PURPLE}")
            wget.download(self.url_chrome)
            print(reset)
            self.system()

    def edge(self):
        if glob("msedgedriver.exe"):
            print(f"\n{reset}{DARKCYAN}Edge Driver'i yüklü. İşlem başlıyor....\n")
            time.sleep(2)
            print(f"Browser Açılıyor{reset}")
            time.sleep(1)
            self.system()
        else:
            print(f"\n{reset}[{RED}!{reset}] {DARKCYAN}Driver Yüklü değil{reset}\n")
            print(f"\t[{RED}-{reset}] {DARKCYAN}İndirme İşlemi Başlıyor{PURPLE}")
            time.sleep(3)
            print(f"{DARKCYAN}\t[{RED}-{DARKCYAN}] İndiriliyor...{PURPLE}")
            wget.download(self.url_edge)
            print(reset)
            self.system()
        
    def system(self):
        if self.q == "1":
            driver = webdriver.Chrome(executable_path="chromedriver.exe")
            driver.get(fast_finger)
            driver.maximize_window()
            self.qq = input(f"{DARKCYAN}Hazır olduğunda {BLUE}B{DARKCYAN}'ye basıp aktif edebilirsin.{reset}").upper()
            driver.implicitly_wait(7)
            if self.qq == "B":
                try:
                    print(f"{BLUE}AKTİF{reset}\n")
                    print(f"{DARKCYAN}BAŞLIYOR\nLütfen açılan tarayıcıyı {BLUE}TAM EKRAN{DARKCYAN} yapın")
                    inpt = driver.find_element_by_xpath("//*[@id='inputfield']")
                    for i in range(1,355):
                        word = driver.find_element_by_xpath(f"//*[@id='row1']/span[{i}]")
                        inpt.send_keys(word.text+" ")
                        time.sleep(0.02)
                        print(f"\033[F\t[{BLUE}-{BLUE}{reset}]{RED}{word.text}{reset}")
                    i = input(f"[{RED}!{reset}] Bitti Çıkış yapmak için enter tuşunu kullan...")
                    if i:exit()
                except selenium.common.exceptions.NoSuchElementException:
                    i = input(f"[{RED}!{reset}] Bitti Çıkış yapmak için enter tuşunu kullan...")
                    if i:exit()
                except selenium.common.exceptions.WebDriverException:
                    print(f"\t[{RED}!{reset}] İlgili Tarayıcı Hata Verdi")

        elif self.q == "2":
            driver = webdriver.Edge(executable_path="msedgedriver.exe")
            driver.get(fast_finger)
            driver.maximize_window()
            self.qq = input(f"{DARKCYAN}Hazır olduğunda {BLUE}B{DARKCYAN}'ye basıp aktif edebilirsin.{reset}").upper()
            driver.implicitly_wait(7)
            if self.qq == "B":
                try:
                    print(f"{BLUE}AKTİF{reset}\n")
                    inpt = driver.find_element_by_xpath("//*[@id='inputfield']")
                    for i in range(1,354):
                        word = driver.find_element_by_xpath(f"//*[@id='row1']/span[{i}]")
                        inpt.send_keys(word.text+" ")
                        time.sleep(0.02)
                        print(f"\033[F\t[{BLUE}-{BLUE}{reset}]{RED}{word.text}{reset}")
                    i = input(f"[{RED}!{reset}] Bitti Çıkış yapmak için enter tuşunu kullan...")
                    if i:exit()
                except selenium.common.exceptions.NoSuchElementException:
                    i = input(f"[{RED}!{reset}] Bitti Eğer Zaman Dolduysa Çıkış yapmak için enter tuşunu kullan...")
                    if i:exit()
                except selenium.common.exceptions.WebDriverException:
                    print(f"\t[{RED}!{reset}] İlgili Tarayıcı Hata Verdi")

    def config(self):
        pass

if __name__ == "__main__":
    print(program_name)
    fast_finger =  "https://10fastfingers.com/typing-test/turkish"
    url_Edge = "https://s7.dosya.tc/en2.php?a=server21/316irl/msedgedriver.exe&b=7a23675a46c4afd2ee4df7e07de2a77e"
    url_Chrome = "https://s2.dosya.tc/en2.php?a=server16/qz8a3n/chromedriver.exe&b=e9a70e040781243d0dfa7ab21a7c69fc"
    print(F"{DARKCYAN}Hangi Tarayıcıyı kullanıyorsun?\n(Şuanlık desteklenen Google Chrome Ve Microsoft Edge){reset}\n\n\t[1] {YELLOW}Chrome{reset}\t[2]{CYAN} Edge{reset}\n\n")
    TenFingerBot(url1=url_Chrome,url2=url_Edge)
