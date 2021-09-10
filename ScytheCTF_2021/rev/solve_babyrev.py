target = '67 7a 62 72 4b 99 bc 84 9d b9 6f 64 83 9a bb 79 5b b5 79 7c 86 ac ae bc 8d 76 b0 b0 6b 7a 60 b3 6b 91 8a 86 6a 6a 61 5f 78 81 8e 6b 91 64 48 4c'

target = target.split()

key = 'finding_keys_has_never_been_easier'

ans = ''

for i in range(len(target)):
    v = int(target[i], 16)
    v += 0x42
    v = v^ord(key[i%0x22])
    v -= ord('i')
    ans += chr(v)

print(ans)
