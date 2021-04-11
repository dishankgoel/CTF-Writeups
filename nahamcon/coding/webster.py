from pwn import *
import enchant
from wordster import wordster

p = remote("jh2i.com", 50012)

def solve(func, real, words):
    ans = []
    for i in words:
        if(enchant.Dict("en_US").check(i) == real):
            ans.append(i)
    if(func == "count"):
        return str(len(ans))
    elif(func == "chrono"):
        return " ".join(ans)
    elif(func == "alpha"):
        ans.sort()
        return " ".join(ans)


while 1:
    query = p.recvline().rstrip()
    print(query)
    if(b"NOT" in query):
        real = False
    else:
        real = True
    if(b"CHRONOLOGICAL" in query):
        func = "chrono"
    elif(b"ALPHABETICAL" in query):
        func = "alpha"
    else:
        func = "count"
    words = p.recvline().rstrip()
    words = [i.decode() for i in words.split()]
    ans = solve(func, real, words)
    p.sendline(ans)
    print(p.recvline())

