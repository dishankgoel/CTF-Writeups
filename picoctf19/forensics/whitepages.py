f = open("whitepages.txt", "rb").read()
i = 0
s = ''
while(i < len(f)):
	if(f[i] == b'\xe2'):
		s += '0'
		i += 3
	elif(f[i] == b'\x20'):
		s += '1'
		i += 1

import binascii

print hex(int(s,2))[3:-1].decode("hex")
