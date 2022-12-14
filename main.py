import time
from subprocess import call
import os
print("""$$$$$$\ $$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\  $$\       $$\        $$$$$$\ $$$$$$$$\ $$$$$$\  $$$$$$\  $$\   $$\ 
\_$$  _|$$$\  $$ |$$  __$$\\__$$  __| $$  __$$\ $$ |      $$ |      $$  __$$\\__$$  __|\_$$  _| $$  __$$\ $$$\  $$ |
  $$ |  $$$$\ $$ |$$ /  \__|  $$ |   $$ /  $$ |$$ |      $$ |      $$ /  $$ |  $$ |     $$ |  $$ /  $$ |$$$$\ $$ |
  $$ |  $$ $$\$$ |\$$$$$$\    $$ |   $$$$$$$$ |$$ |      $$ |      $$$$$$$$ |  $$ |     $$ |  $$ |  $$ |$$ $$\$$ |
  $$ |  $$ \$$$$ | \____$$\   $$ |   $$  __$$ |$$ |      $$ |      $$  __$$ |  $$ |     $$ |  $$ |  $$ |$$ \$$$$ |
  $$ |  $$ |\$$$ |$$\   $$ |  $$ |   $$ |  $$ |$$ |      $$ |      $$ |  $$ |  $$ |     $$ |  $$ |  $$ |$$ |\$$$ |
$$$$$$\ $$ | \$$ |\$$$$$$  |  $$ |   $$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$ |  $$ |  $$ |   $$$$$$\  $$$$$$  |$$ | \$$ |
\______|\__|  \__| \______/   \__|   \__|  \__|\________|\________|\__|  \__|  \__|   \______| \______/ \__|  \__|
                                                                                                                  
                                                                                                                  
                                                                                                                  
""")
print("Install?")
time.sleep(0.5)
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
    print("Running script in 10 Secounds")
    time.sleep(10)
    call(["python", "LMAO.py"])



if choice == "no":
    call(["python", "fail.py"])
    
