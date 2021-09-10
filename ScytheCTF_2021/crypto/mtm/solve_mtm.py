#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import getPrime
import random
import hashlib
import os
import sys
from binascii import unhexlify

shared_secret = 194665809154021303263595634629038226528

sha1 = hashlib.sha1()
sha1.update(str(shared_secret).encode('ascii'))
key = sha1.digest()[:16] # key generated from shared secret 

iv = b'a161444b2c4e5ffed960060a263bfec3'
encrypted = b'7cc2a8c07ed6341432c9d6598e7c2b916e206161b297d9e32f409c08b6bbdf9ed373c518066f17d4f82297fc0742309d'

iv = unhexlify(iv)
encrypted = unhexlify(encrypted)

cipher = AES.new(key, AES.MODE_CBC, iv)
flag = cipher.decrypt(encrypted)
print(flag)