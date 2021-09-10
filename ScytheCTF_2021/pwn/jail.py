#! /usr/bin/python3

def main():
    while True :
        text = input("[+] ")
        text=text.lower()
        for keyword in ["eval", "exec", "open", "read","write","import","os","subprocess","shlex","sh"]:
            if keyword in text:
                print(f"Got this one ;) {keyword} !")
                return
        else:
            exec(text)

if __name__ == "__main__":
    main()