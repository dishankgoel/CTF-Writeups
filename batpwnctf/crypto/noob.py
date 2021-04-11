#!/usr/bin/env python2
# I AM NOOB :)
import string
from hashlib import md5
# from itertools import izip, cycle
import base64
import time

target = open('noob.txt').read()

up = int(1589483286.6927943)
lower = int(1589396889.9810355)

def xor(data, key): 
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key]))) 

flag=base64.b64decode(target)
   
# timestamp = time.time()
# print int(timestamp)
for timestamp in range(lower, up):
    key = md5(str(int(timestamp))).hexdigest()
    my_hexdata = key

    scale = 16 
    num_of_bits = 8
    noobda = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
    # print noobda
    xorer = xor(flag,noobda)
    noobie = base64.encodestring(xorer).strip()
    if("batpwn{" in xorer):
        print("Found!!!")
        print("Flag: {}".format(xorer))
# print noobie



