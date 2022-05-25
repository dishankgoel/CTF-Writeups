from binascii import unhexlify

def rev_one(o):
    return "".join([chr(ord(o[i]) - i) for i in range(len(o))])

def rev_two(o):
    return "".join([chr(ord(o[i])^i) for i in range(len(o))])

def rev_three(o):
    return "".join([chr(ord(o[i]) + i + 7) for i in range(len(o))])

def one(inp):
    return "".join([chr(ord(inp[i]) - i) for i in range(len(inp))])

def two(inp):
    return "".join([chr(ord(inp[i])^i) for i in range(len(inp))])

def three(inp):
    return "".join([chr(ord(inp[i]) + i + 7) for i in range(len(inp))])

in1 = unhexlify("6b5a613c").decode()[::-1]
in1 += unhexlify("5e60").decode()[::-1]
# case1 = rev_two(rev_two(rev_one(rev_three(in1))))
case1 = rev_three(rev_one(rev_two(rev_two(in1))))

in2 = unhexlify("6e5a653b").decode()[::-1]
in2 += unhexlify("75").decode()[::-1]
# case2 = rev_three(rev_one(rev_two(rev_one(in2))))
case2 = rev_one(rev_two(rev_one(rev_three(in2))))

in3 = unhexlify("57525f36").decode()[::-1]
in3 += unhexlify("57").decode()[::-1]
# case3 = rev_three(rev_one(rev_two(rev_three(in3))))
case3 = rev_three(rev_two(rev_one(rev_three(in3))))

in4 = unhexlify("59516144").decode()[::-1]
in4 += unhexlify("6457").decode()[::-1]
# case4 = rev_two(rev_three(rev_one(rev_three(in4))))
case4 = rev_three(rev_one(rev_three(rev_two(in4))))

in5 = unhexlify("66515f34").decode()[::-1]
in5 += unhexlify("62").decode()[::-1]
# case5 = rev_two(rev_three(rev_one(rev_one(in5))))
case5 = rev_three(rev_one(rev_one(rev_three(rev_two(in5)))))

in6 = unhexlify("6b5a613c").decode()[::-1]
in6 += unhexlify("5e60").decode()[::-1]
# case6 = rev_two(rev_two(rev_one(rev_three(in6))))
case6 = rev_three(rev_one(rev_two(rev_two(in6))))

in7 = unhexlify("6b766b46").decode()[::-1]
in7 += unhexlify("31").decode()[::-1]
# case7 = rev_one(rev_two(rev_one(rev_one(in7))))
case7 = rev_one(rev_one(rev_two(rev_one(in7))))

print(case1)
print(case2)
print(case3)
print(case4)
print(case5)
print(case6)
print(case7)
