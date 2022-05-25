import os
import random
from string import ascii_lowercase

num = 1000
init_file = "flag.txt"
os.system("zip -r fhiwff0923.zip flag.txt")
prev_name = "fhiwff0923"
for i in range(1, num + 1):
    name = "".join([random.choice(ascii_lowercase) for i in range(16)])
    os.system("zip -r {}.zip {}.zip message.txt && rm {}.zip".format(name, prev_name, prev_name))
    prev_name = name
