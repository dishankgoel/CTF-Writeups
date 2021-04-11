#!/usr/bin/python

import random
from Crypto.Cipher import AES
from os import urandom
from string import printable
given = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'

flag = 'fa364f11360cef2550bd9426948af22919f8bdf4903ee561ba3d9b9c7daba4e759268b5b5b4ea2589af3cf4abe6f9ae7e33c84e73a9c1630a25752ad2a984abfbbfaca24f7c0b4313e87e396f2bf5ae56ee99bb03c2ffdf67072e1dc98f9ef691db700d73f85f57ebd84f5c1711a28d1a50787d6e1b5e726bc50db5a3694f576'
k = 2**32
s = k/(2**8)
while(s <= k):
    random.seed(s)
    print(s)
    key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
    key2 = ''.join([random.choice(printable) for _ in range(3)]) + '0'*13

    cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
    cipher2 = AES.new(key=key2, mode=AES.MODE_ECB)

    print "\nGive me a string:"
    pt = 'aaaaaaaaaaaaaaaa'

    val = len(pt) % 16
    if not val == 0:
        pt += '0'*(16 - val)

    c1 = cipher1.encrypt(pt.encode('hex'))
    c2 = cipher2.encrypt(c1.encode('hex'))
    print 'Encrypted string:\n' + c2.encode('hex')
    if(c2.encode('hex') == given):
        a1 = cipher2.decrypt(flag.decode('hex'))
        b1 = cipher1.decrypt(a1.decode('hex'))
        print(b1)
        print(b1.decode('hex'))
        print(s)
        input()
    s += 1

    # with open("flag.txt") as f:
    #     flag = f.read().strip()
    # # length of flag is a multiple of 16
    # ct1 = cipher1.encrypt(flag.encode('hex'))
    # ct2 = cipher2.encrypt(ct1.encode('hex'))
    # print '\nEncrypted Flag:\n' + ct2.encode('hex') + '\n'