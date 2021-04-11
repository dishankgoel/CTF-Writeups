from random import choice, randint
from string import ascii_letters
from itertools import cycle

key = 'hexCTF{'

f = open('flag.enc', 'rb').read()

for i in range(len(f) - len(key)):
    t = ''
    for j in range(len(key)):
        t += chr(f[i+j]^ord(key[j]))
    print(t)