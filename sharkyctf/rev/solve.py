some_array = "0a 02 1e 0f 03 07 04 02 01 18 05 0b 18 04 0e 0d 05 06 13 14 17 09 0a 02 1e 0f 03 07 04 02 01 18".split()
second_array = "57 40 a3 78 7d 67 55 40 1e ae 5b 11 5d 40 aa 17 58 4f 7e 4d 4e 42 5d 51 57 5f 5f 12 1d 5a 4f bf".split()

n = len(some_array)
flag = ''

for i in range(n):
    c = ((int(second_array[i],16)^0x2a)%256 - int(some_array[i], 16))%256
    flag += chr(c)

print(flag)
print(len(flag))

