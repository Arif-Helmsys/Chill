import string
import random
from time import sleep, time

letters = list(string.printable)
input_ = input("Parola oluştur: ")
passw = ""
ilk = time()
while input_ != passw:
    sleep(0.3)
    try_again = random.choices(letters,k=len(input_))
    (lambda: [try_again.remove(j) for j in try_again if j in list(string.whitespace)])()
    for i in try_again:
        if i in input_:
            passw += i
    if input_ == passw:
        print(passw)
        print("Bulundu")
        print(f"{(son-ilk).__round__(3)} Saniye sürdü")
    else:
        print(f"Denendi : {try_again}")
    son = time()
