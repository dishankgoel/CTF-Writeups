from binascii import unhexlify

def bytes_to_bits(inp):
    res = []
    for v in inp:
        res.extend(list(map(int, format(v, '08b'))))
    return res

def bits_to_bytes(inp):
    res = []
    for i in range(0, len(inp), 8):
        res.append(int(''.join(map(str, inp[i:i+8])), 2))
    return bytes(res)

def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

f = 'output.txt'
enc = open(f).readlines()[0][:-1]
enc = unhexlify(enc)
public = eval(open(f).readlines()[1])

enc = bytes_to_bits(enc)
n = len(enc)
print(n)
print(len(public))
# assert n == len(public)
keystream = [0 for i in range(len(public))]

print(len(public))

d = {}
for i in range(len(public)):
    d[public[i][0]] = [1, i, public[i][1]]
    d[public[i][1]] = [0, i, public[i][0]]

# last n//3 column
mid_key = []
for i in range(len(public)):
    val = public[i][0]^public[i][1]
    if val in d:
        keystream[d[val][1]] = d[val][0]
        mid_key.append(d[val][2])


mid_key = list(set(mid_key))
# middle n//3 column
first_key = []
for i in range(len(public)):
    for key_val in mid_key:
        val = public[i][0]^public[i][1]^key_val
        if val in d:
            keystream[d[val][1]] = d[val][0]
            first_key.append(d[val][2])

# first n//3 column
first_key = list(set(first_key))
for i in range(len(public)):
    for key_val in first_key:
        val = public[i][0]^public[i][1]^key_val
        if val in d:
            keystream[d[val][1]] = d[val][0]
            mid_key.append(d[val][2])
print(keystream)
print(bits_to_bytes(xor(keystream, enc)))
