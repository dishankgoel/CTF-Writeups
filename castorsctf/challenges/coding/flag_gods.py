import hashlib
from binascii import unhexlify,hexlify
from pwn import *

def conv(s):
    return bin(int(hexlify(s),16))[2:]

def hamming_distance(string1, string2): 
    string1 = conv(string1)
    string2 = conv(string2).zfill(len(string1))
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance

p = remote("chals20.cybercastors.com" ,14431)

text = p.recvuntil("ready.")

p.sendline("\n")

while 1:
    try:
        msg = p.recvuntil("distance:").split()
    except:
        p.interactive()

    str1 = b''
    str2 = b''

    start = 8
    for i in range(start, len(msg)):
        if(msg[i] == b'Received'):
            break
        else:
            str1 += msg[i] + b" "

    str1 = str1.rstrip()
    str2 = unhexlify(msg[-4])
    print(str1)
    print(str2)
    ans = hamming_distance(str1, str2)
    print(ans)
    p.sendline(str(ans))

    p.recvuntil("answer!")
