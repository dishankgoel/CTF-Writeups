from pwn import *
f=open("flag.bmp","rb").read() 
f=f[6:] # good luck finding these missing pieces :p
padding=bytes(16-len(f)%16) #motivation from block cipher schemes
f+=padding 
cdata=f[:16]
for i in range(16,len(f),16):
    cdata+=xor(f[i:i+16],cdata[i-16:i]) #xoring and xoring ..

print(open('corrupted.bmp','wb').write(cdata))
