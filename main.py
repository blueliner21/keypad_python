import machine
import time
#from ssd1306 import SSD1306_I2C

#6-13-23 To Do: Add code check algo. Print to OLED 

R1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
R2 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)
R3 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
R4 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)

C1 = machine.Pin(20, machine.Pin.OUT)
C2 = machine.Pin(21, machine.Pin.OUT)
C3 = machine.Pin(22, machine.Pin.OUT)

code = []
code.clear()
def enter_pressed():
    print(code)
    for items in code:
        print(code[items])
    
    

while True:
    C1.value(1)
    if R1.value():
        #print("7")
        code.append(7)
        time.sleep_ms(250)
    if R2.value():
        #print("4")
        code.append(4)
        time.sleep_ms(250)
    if R3.value():
        #print("1")
        code.append(1)
        time.sleep_ms(250)
    if R4.value():
        print("CLEAR")
        code.clear()
        time.sleep_ms(250)
    C1.value(0)
    C2.value(1)
    if R1.value():
        #print("8")
        code.append(8)
        time.sleep_ms(250)
    if R2.value():
        #print("5")
        code.append(5)
        time.sleep_ms(250)
    if R3.value():
        #print("2")
        code.append(2)
        time.sleep_ms(250)
    if R4.value():
        #print("0")
        code.append(0)
        time.sleep_ms(250)
    C2.value(0)
    C3.value(1)
    if R1.value():
        #print("9")
        code.append(9)
        time.sleep_ms(250)
    if R2.value():
        #print("6")
        code.append(6)
        time.sleep_ms(250)
    if R3.value():
        #print("3")
        code.append(3)
        time.sleep_ms(250)
    if R4.value():
        #print("Enter")
        enter_pressed()
        time.sleep_ms(250)
    C3.value(0)
