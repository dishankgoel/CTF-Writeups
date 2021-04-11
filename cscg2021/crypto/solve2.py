from binascii import hexlify, unhexlify


def int_to_bytes(i):
    return i.to_bytes((i.bit_length() + 7) // 8, 'big')


c = '6368616c6c656e67655f33303435343230353736386539343934'

c = unhexlify(c)

c = c.replace(b"_",  bytes(chr(ord("_") - 1), "utf-8"))

c = hexlify(c)
print(c)