from pwn import *


# p = remote('arthurashe.ctf.umbccd.io', 8411)

# p.recvuntil('?')
# p.sendline('y')
# bits = ''
# while 1:
#     try:
#         s = p.recvuntil('.').split()
#     except:
#         print(bits)
#         k = hex(int(bits, 2))[2:]
#         flag = "".join([chr(int(k[i:i+2], 16)) for i in range(len(k))])
#         print(flag)
#         p.interactive()


#     print(s)
#     k = str(s[-1],'utf-8').split('-')
#     l = k[0]
#     r = k[1][:-1]

#     if(l == 'love'):
#         l = '0'
#     if(r == 'love'):
#         r = '0'

#     if(l == 'game'):
#         p.sendline('0')
#         bits += '0'
#     elif(r == 'game'):
#         p.sendline('1')
#         bits += '1'
#     elif(l == 'set'):
#         p.sendline('0')
#         bits += '0'
#     elif(r == 'set'):
#         p.sendline('1')
#         bits += '1'
#     else:
#         try:
#             if(int(l) > int(r)):
#                 p.sendline('0')
#                 bits += '0'
#             else:
#                 p.sendline('1')
#                 bits += '1'
#         except:
#             print(l, r)

# bits = 'TFheR \x04FflÆa\x16gr \x06is2 \x04DFa\x17wvgtC5TDFg{´LÃ0\x07vc35_ôMÖeT@\x06nã5U_ôNã0\x037vh1\x16nægu_ò!\x16nå_õTB#6eU_ôGt@\x06mÓ35_ôOöfe_õTC36nænã1\x135R.ç}Ò.\x0e'
bits = '010101000110100001100101001000000100011001101100011000010110011100100000011010010111001100100000010001000110000101110111011001110100001101010100010001100111101101001100001100000111011000110011010111110100110101100101010000000110111000110101010111110100111000110000001101110110100000110001011011100110011101011111001000010110111001011111010101000010001101100101010111110100011101000000011011010011001101011111010011110110011001011111010101000011001101101110011011100011000100110101001011100111110100101110'

orig = ''
for i in bits:
    if(i == '0'):
        orig += '1'
    else:
        orig += '0'

k = hex(int(bits, 2))[2:]
flag = "".join([chr(int(k[i:i+2], 16)) for i in range(0,len(k),2)])
print(flag)