from binascii import unhexlify

c = "ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c"

c = unhexlify(c)

known_plaintext = b"actf{"

for i in range(len(c) - 5):
    key = ""
    for j in range(i, i + 5):
        key += chr(known_plaintext[j - i]^c[j])
    plain_text = "".join([chr(c[k]^ord(key[k%5])) for k in range(len(c))])
    print(plain_text)

