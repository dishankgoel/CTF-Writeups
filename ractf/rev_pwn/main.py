from binascii import unhexlify

flag = 'fqtbjfub4uj_0_d00151a52523e510f3e50521814141c'

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def encrypt(a):
    some_text = a[::2]

    randnum = 14
    text_length = len(some_text)
    endtext = ""
    for i in range(1, text_length + 1):
      weirdtext = some_text[i - 1]
      if weirdtext >= "a" and weirdtext <= "z":
          weirdtext = chr(ord(weirdtext) + randnum)
          if weirdtext > "z":
              weirdtext = chr(ord(weirdtext) - 26)
      endtext += weirdtext
    randtext = a[1::2]

    xored = xor("aaaaaaaaaaaaaaa", randtext)
    hex_xored = xored.encode("utf-8").hex()

    return endtext + hex_xored

def decrypt(msg):
    first = msg[:-30]
    second = msg[-30:]
    second = xor(unhexlify(second).decode('utf-8'), "aaaaaaaaaaaaaaa")
    new_first = ['']*len(first)
    for i in range(len(first)):
        if(chr(ord(first[i]) + 26)  > "z"):
            new_first[i] = chr(ord(first[i]) + 26)
        else:
            new_first[i] = chr(ord(first[i]))
        ifchar = chr(ord(new_first[i]) - 14)
        if(ifchar >= "a" and ifchar <= "z"):
            new_first[i] = ifchar
        else:
            new_first[i] = first[i]
    flag = ''
    for i in range(len(new_first) + len(second)):
        if(i%2 == 0):
            flag += new_first[i//2]
        else:
            flag += second[i//2]
    print(flag)
    print("".join(new_first))
    print(second)



    # print("".join([chr(ord(i) - 14) for i in first]))

decrypt(flag)
# def main():
#     opt = input("Would you like to [E]ncrypt or [D]ecrypt? ")
#     if opt[:1].lower() == "e":
#         msg = input("Enter message to encrypt: ")
#         print(f"Encrypted message: {encrypt(msg)}")
#     elif opt[:1].lower() == "d":
#         msg = input("Enter message to decrypt: ")
#         print(f"Decrypted message: {decrypt(msg)}")

# if __name__ == "__main__":
#     main()
