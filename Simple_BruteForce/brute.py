import itertools
import time
import os

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

reset = END

print(f"""{PURPLE}{BOLD}
                    SIMPLE
   ______                  ________)
  (, /    )               (, /                 
    /---(  __     _/_  _    /___, _____  _   _ 
 ) / ____)/ (_(_(_(___(/_) /     (_)/ (_(___(/_
(_/ (                   (_/                    
                coding Helmsys
\n""")
password = list(str(input(f"{GREEN}[+] Please Create Your Password In Here >>> {RED}")))
def BruteForce():
    count = 0
    print("Creating Wordlist...")
    with open("wordlist.txt","w",encoding="utf-8") as f:
        for i in itertools.product(password,repeat=len(password)):
            f.write(str(list(i))+"\n")
    A = time.time()
    with open("wordlist.txt","r",encoding="utf-8") as g:
        readd = g.readlines()
    for _ in readd:
        sj = readd[count].strip()
        if sj == str(password):
            print(f"""{RED}[{CYAN}+{CYAN}{RED}] Your Password is < {CYAN}{BOLD}{sj.replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")}{CYAN}{RED} >""")
            break
        else:
            print(f"\t{GREEN}[-] Trying... {sj}")
            count += 1
    os.remove("wordlist.txt")
    B = time.time()
    print(f"{GREEN}[+] Completed In {RED}{(B-A).__round__(3)}{GREEN} Seconds{reset}")
    ext = input("\t[-] To exit, press any key and then enter...")
    if ext:
        exit()

if __name__ == "__main__":
    BruteForce()
