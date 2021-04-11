from pwn import *

p = remote("chals20.cybercastors.com" ,14429)

p.recv()
p.sendline("\n")
while 1:
    eq = p.recv().split()
    eq = (eq[2] + eq[3] + eq[4]).decode('utf-8')
    print(eq)
    eq = eq.replace("one", "1")
    eq = eq.replace("two", "2")
    eq = eq.replace("three", "3")
    eq = eq.replace("four", "4")
    eq = eq.replace("five", "5")
    eq = eq.replace("six", "6")
    eq = eq.replace("seven", "7")
    eq = eq.replace("eight", "8")
    eq = eq.replace("nine", "9")
    eq = eq.replace("ten", "10")
    eq = eq.replace("plus", "+")
    eq = eq.replace("minus", "-")
    eq = eq.replace("multiplied-by", "*")
    eq = eq.replace("divided-by", "//")
    ans = eval(eq)
    print(ans)
    p.sendline(str(ans))

    print(p.recv())