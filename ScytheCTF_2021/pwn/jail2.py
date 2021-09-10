#! /usr/bin/python3

def main():
    while True :
        text = input("[+] ")
        text=text.lower()
        for keyword in ["eval", "exec", "open", "read", "write","os","subprocess","shlex","sh","builtins","+","."]:
            if keyword in text:
                print(f"No trespassing : {keyword} !")
                return
        else:
            exec(text)

if __name__ == "__main__":
    main()