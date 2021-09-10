import os

def extract(name):
    os.system(f"7z e -y {name}")
    os.system(f"rm {name}")


while True:
    for d in os.listdir():
        if d.endswith(".zip"):
            extract(d)
            print(d)

