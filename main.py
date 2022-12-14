import time
from subprocess import call
import os
print("Install Script?")
time.sleep(2)
print("yes / no")

choice = input("")

if choice == "yes":
    time.sleep(0.05)
    os.system('pip3 install psutil')
    os.system('pip3 install gputil')
    os.system('pip3 install tabulate')
    os.system('pip3 install cryptography')
    os.system('pip install AppOpener')
    time.sleep(2)
    print("Would you like to see more Tools, Viruses, and Hacks?")
    import os

    choice = input("")

    if choice == "yes":
        time.sleep(0.05)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("OK")
        time.sleep(2)
        print("https://CPScript/Tools")
        time.sleep(2)
        print("Running script in 10 Secounds")
        time.sleep(10)
        call(["python", "LMAO.py"])

    if choice == "no":
        call(["python", "fail.py"])

      

if choice == "no":
    call(["python", "fail.py"])
    
