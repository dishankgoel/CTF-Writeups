from pwn import *
data = open('corrupted.bmp', 'rb').read()

orig = data[:16]
curr = orig
for i in range(16, len(data), 16):
    new_part = xor(data[i:i+16], curr)
    curr = data[i:i+16]
    orig += new_part

orig = b'\x42\x4d' + b'\x00\x00\x00\x00' + orig

open('fixed.bmp', 'wb').write(orig)
