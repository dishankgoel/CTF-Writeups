import magic
import zipfile
import io
import tarfile
import gzip

passwords = ["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein", "696969", "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "pussy", "superman", "1qaz2wsx", "7777777", "fuckyou", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "fuckme", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "asshole", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "fuck", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "6969", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor"]

f = open('1816', 'rb').read()
curr = 1816

while True:
    filetype = magic.from_buffer(f)
    if 'Zip' in filetype:
        z = zipfile.ZipFile(io.BytesIO(f))
        try:
            f = z.read(z.infolist()[0])
        except:
            for pwd in passwords:
                z.setpassword(bytes(pwd, 'utf-8'))
                try:
                    f = z.read(z.infolist()[0])
                    break
                except:
                    continue
    elif 'tar' in filetype:
        tar = tarfile.open(fileobj=io.BytesIO(f), mode='r:*')
        for member in tar.getmembers():
            f = tar.extractfile(member).read()

    elif 'gzip' in filetype:
        f = gzip.decompress(f)
    
    else:
        print(f)
        input()
    print(magic.from_buffer(f))