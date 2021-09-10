#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import getPrime
import random
import hashlib
import os
import sys
FLAG = b'flag{<redacted>}'

def encrypt_flag(shared_secret: int):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16] # key generated from shared secret 
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(FLAG, 16))
    print("[+] IV = ", iv.hex())
    print("[+] encrypted_flag = " , ciphertext.hex())

if __name__=='__main__':
    p=getPrime(128) # 128-bit prime for modulus
    g=2 # generator 
    print("#"*150)
    print("\n Ever got hyped about man-in-the-middle attack in your teenage days ?\n Well , here is your chance to actually pwn this convo bw alice and bob .\n")
    print("#"*150)
    alice_key= random.randint(2,p-1)
    alice_pub= pow(g,alice_key,p)
    print("[+] Alice initiates handshake : ")
    print(f"\n Hey bob , here is my public key :g={g} , p={p} , A = {alice_pub} . Send me yours .\n")
    print("[-] Obviously , It has to go through us before it goes to bob . p and g will be sent as they are.")
    pwn1=int(input("[-] Enter value of A for Bob: "))
    if pwn1 not in range(2,p-1):
        sys.exit("Nope . Try again ")
    print(f"[+] sent to bob !")
    print("#"*150)
    bob_key=random.randint(2,p-1)
    bob_pub=pow(g,bob_key,p)
    print("[+] Bob returns a response :")
    print(f"\n Hey Alice , I got your public key : A = {pwn1} .\n Here is my public key : B = {bob_pub} . Its time for us to make our shared secret ;).\n ")
    print("[-] What should we send back to alice ?")
    pwn2=int(input("[-] Enter here : "))
    if pwn2 not in range(2,p-1):
        sys.exit("Nope . Try again ")
    print(f"[+] Alice got B = {pwn2}")
    shared_secret=pow(pwn2,alice_key,p) # shared secret for Bob .
    print(f"[+] Alice says : I am sending you our top secret . Good luck , Bob .")
    encrypt_flag(shared_secret)





    
