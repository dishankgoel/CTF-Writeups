import hashlib
import Crypto.Util.number as cun
from Crypto.Cipher import AES
from binascii import unhexlify

def diffie_hellman(message: bytes):

    shared_secret = 5312314485985980052876581387572508004398320168183082366968844361369254712474058316954583954524704424138741600958002382989691980819380299479894387238834962
    # Use AES, a symmetric cipher, to encrypt the flag using the shared key
    key = hashlib.sha1(cun.long_to_bytes(shared_secret)).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.decrypt(message)
    print(f"ciphertext = {ciphertext}")

ciphertext = "2e3d187c78c1cf4585cc6d053c021ce3bba1b26912a6dabaa73cac50301738e526af9809bb8de2c41a51a569cfea605d6c745caacd933be79349261573124c57"
diffie_hellman(unhexlify(ciphertext))
