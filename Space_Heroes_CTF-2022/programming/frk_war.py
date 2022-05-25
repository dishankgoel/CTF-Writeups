from pwn import *


p = remote("0.cloud.chals.io", 29511)

mappings = p.recvuntil(b"================================================================================================================")
l = mappings.split(b"\n")[1:-1]
map = {}
for m in l:
    a = m.split(b"]")
    map[a[0].strip() + b"]"] = a[1].strip()

# print(map)
for i in map:
    print(i)

while True:
    ask = p.recvuntil(b">")
    a =  ask.split(b"\n")
    cords = b"[" + a[1].split(b"[")[1]
    print(map[cords])
    input()

# p.interactive()
