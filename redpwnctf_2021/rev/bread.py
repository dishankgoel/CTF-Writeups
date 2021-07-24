from pwn import *

#p = process("./bread")
p = remote("mc.ax", 31796)
def send_ins(ins):
    response = p.recv()
    print(response)
    p.sendline(ins)

send_ins("add flour")
send_ins("add yeast")
send_ins("add salt")
send_ins("add water")

send_ins("hide the bowl inside a box")

send_ins("wait 3 hours")

send_ins("work in the basement")

send_ins("preheat the toaster oven")

send_ins("set a timer on your phone")

send_ins("watch the bread bake")

send_ins("pull the tray out with a towel")

send_ins("unplug the oven")
send_ins("open the window")
send_ins("unplug the fire alarm")

send_ins("wash the sink")
send_ins("clean the counters")
send_ins("flush the bread down the toilet")
send_ins("get ready to sleep")

send_ins("close the window")
send_ins("replace the fire alarm")
send_ins("brush teeth and go to bed")

p.interactive()
