from binascii import unhexlify
inp = "ABCDEFGHIJKLMNO"
final = b'D^Bi~0sv\257\060\204hZGH'

# inp = 'abcdefghijklmno'
# final = b'$~\242\b\236Q\023VO0dH:g(b'

inp = 'CTF{abcdefghij}'
final = b'$|\254\b\231YP\256\060`m\n\\2\021\060\336\377\377\377'[:15]
# final = b'Cz\246z\202]\027Df0`L&[4'

inp = 'TbcCagejF}{dfhi'

shuffle = ["02", "06", "07", "01", "05", "0b", "09", "0e", "03", "0f", "04", "08", "0a", "0c", "0d"]
add = ["ef","be","ad","de","ad","de","e1","fe","37","13","37","13","66","74","63","67"]
xor = ["76", "58", "b4", "49", "8d", "1a", "5f", "38", "d4", "23", "f8", "34", "eb", "86", "f9", "aa"]

def xor_two(inp):
    ans = ''
    for i in range(len(inp)):
        ans += chr(int(xor[i],16)^inp[i])
    return ans

def sub(inp):
    ans = ''
    for i in range(len(inp)):
        ans += chr((ord(inp[i]) - int(add[i],16))%256)
    return ans

def anti_shuffle(final_out):
    ans = [0 for i in range(len(final_out))]
    for i in range(len(final_out)):
        ans[i] = final_out[int(shuffle[i],16) - 1]
    return ''.join(ans)


print(len(final))
undo_xor = xor_two(final)
print(len(undo_xor))
undo_add = sub(undo_xor)
print(len(undo_add))
print(undo_add)
print(anti_shuffle(inp))
