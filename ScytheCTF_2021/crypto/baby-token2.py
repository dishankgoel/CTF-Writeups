#!/usr/bin/python3

import jwt # I am using PyJWT version 0.4.3 ,will update this asap 
import sys

with open('./private-key.pem', 'rb') as f:
   PRIVATE_KEY = f.read()
with open('./public-key.pem', 'rb') as f:
   PUBLIC_KEY = f.read()

FLAG = b'flag{<redacted>}'

def authorise(token):
    try:
        decoded = jwt.decode(token, PUBLIC_KEY)
    except Exception as e:
        return {"error": str(e)}
    if "admin" in decoded and decoded["admin"] =='True':
        return {"response": f"All hail admin , here is your flag: {FLAG}"}
    elif "username" in decoded:
        return {"response": f"Bonsoir {decoded['username']}"}
    else:
        return {"error": "dunno what got wrong.. zzz"}

def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': False}, PRIVATE_KEY)
    return {"session": encoded.decode()}

def get_pubkey():
    return {"pubkey": PRIVATE_KEY} # oops , I hope nobody notices this  


if __name__=='__main__':
    while True:
        print("""\n[+] MENU :\n1. Authorise\n2. Create token\n3. Get Public Key\n4. Quit\n""")
        sys.stdout.flush()
        options=int(input('[+] What is your choice : '))
        if options == 1:
            token=input('[-] Enter token :')
            print(authorise(token))
            sys.stdout.flush()
        elif options == 2:
            user=input('[-] Enter the username : ')
            print(create_session(user))
            sys.stdout.flush()
        elif options == 3 :
            print(get_pubkey())
            sys.stdout.flush()
        elif options == 4:
            sys.exit("See you again ..")
