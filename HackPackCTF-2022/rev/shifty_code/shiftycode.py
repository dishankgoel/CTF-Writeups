program = open("bin", "rb").read()
print("Read program: ", len(program))

stack = [0 for i in range(256)]
commands = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def error():
    print("Something wrong happened")
    exit()

def execute(my_inp):
    val = program[0]
    ptr = 1
    reg = 0
    inp_ptr = 0
    while True:
        if(val == commands[0]):
            print("[*] Adding:\t", end='')
            commands[0] += 1
            if(program[ptr] == 1):
                stack[program[ptr + 1]] += program[ptr + 2]
                print("stack[{}] += {}".format(program[ptr + 1], program[ptr + 2]))
            elif(program[ptr] == 2):
                stack[program[ptr + 1]] += stack[program[ptr + 2]]
                print("stack[{}] += stack[{}], value = {}".format(program[ptr + 1], program[ptr + 2], stack[program[ptr + 2]]))
            else:
                error()
            ptr += 3
        elif(val == commands[1]):
            print("[*] Subtract:\t", end='')
            commands[1] += 1
            if(program[ptr] == 1):
                stack[program[ptr + 1]] -= program[ptr + 2]
                print("stack[{}] -= {}".format(program[ptr + 1], program[ptr + 2]))
            elif(program[ptr] == 2):
                stack[program[ptr + 1]] -= stack[program[ptr + 2]]
                print("stack[{}] -= stack[{}]".format(program[ptr + 1], program[ptr + 2]))
            else:
                error()
            ptr += 3
        elif(val == commands[2]):
            print("[*] Multipling:\t", end='')
            commands[2] += 1
            if(program[ptr] == 1):
                stack[program[ptr + 1]] *= program[ptr + 2]
                print("stack[{}] *= {}".format(program[ptr + 1], program[ptr + 2]))
            elif(program[ptr] == 2):
                stack[program[ptr + 1]] *= stack[program[ptr + 2]]
                print("stack[{}] *= stack[{}]".format(program[ptr + 1], program[ptr + 2]))
            else:
                error()
            ptr += 3
        elif(val == commands[3]):
            print("[*] Dividing:\t", end='')
            commands[3] += 1
            if(program[ptr] == 1):
                stack[program[ptr + 1]] /= program[ptr + 2]
                print("stack[{}] /= {}".format(program[ptr + 1], program[ptr + 2]))
            elif(program[ptr] == 2):
                stack[program[ptr + 1]] /= stack[program[ptr + 2]]
                print("stack[{}] /= stack[{}]".format(program[ptr + 1], program[ptr + 2]))
            else:
                error()
            ptr += 3
        elif(val == commands[4]):
            print("[*] Printing")
            print(stack[program[ptr]])
        elif(val == commands[5]):
            print("[*] Branching:\t", end='')
            commands[5] += 1
            if(program[ptr] == 1):
                print("reg == 0, actual value: ", reg)
                ptr = ptr + 2
                if(reg != 0):
                    ptr += program[ptr + 1]
            elif(program[ptr] == 2):
                print("reg != 0")
                ptr = ptr + 2
                if(reg == 0):
                    ptr += program[ptr + 1]
            else:
                error()
        elif(val == commands[6]):
            commands[6] += 1
            inp = my_inp[inp_ptr]
            print("[*] Giving input: ", inp)
            stack[program[ptr]] = inp
            ptr += 1
            inp_ptr += 1
        elif(val == commands[7]):
            print("[*] Comparing:\t", end='')
            commands[7] += 1
            if(program[ptr] == 1):
                print("stack[{}] == {}".format(program[ptr + 1], program[ptr + 2]))
                if(stack[program[ptr + 1]] == program[ptr + 2]):
                    reg = 0
                else:
                    reg = 1
                ptr += 3
            elif(program[ptr] == 2):
                print("stack[{}] == stack[{}]".format(program[ptr + 1], program[ptr + 2]))
                if(stack[program[ptr + 1]] == stack[program[ptr + 2]]):
                    reg = 0
                else:
                    reg = 1
                ptr += 3
            elif(program[ptr] == 3):
                print("stack[{}] < {}".format(program[ptr + 1], program[ptr + 2]))
                if(stack[program[ptr + 1]] < program[ptr + 2]):
                    reg = 0
                else:
                    reg = 1
                ptr += 3
            elif(program[ptr] == 4):
                print("stack[{}] > {}".format(program[ptr + 1], program[ptr + 2]))
                if(stack[program[ptr + 1]] > program[ptr + 2]):
                    reg = 0
                else:
                    reg = 1
                ptr += 3
            elif(program[ptr] == 5):
                print("stack[{}] < stack[{}]".format(program[ptr + 1], program[ptr + 2]))
                if(stack[program[ptr + 1]] < stack[program[ptr + 2]]):
                    reg = 0
                else:
                    reg = 1
                ptr += 3
            elif(program[ptr] == 6):
                print("stack[{}] > stack[{}]".format(program[ptr + 1], program[ptr + 2]))
                if(stack[program[ptr + 1]] > stack[program[ptr + 2]]):
                    reg = 0
                else:
                    reg = 1
                ptr += 3
            else:
                error()
        elif(val == commands[8]):
            print("Program exited")
            break
        val = program[ptr]
        ptr += 1

# my_inp = b"flag{abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYXY}"
#                                  |24
my_inp = b"flag{my_sh1fti35_453_n1fty}"
my_inp += b"A"*30
execute(my_inp)
