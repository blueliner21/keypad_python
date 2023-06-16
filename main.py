import machine
import time
from ssd1306 import SSD1306_SPI

#Code 144965
#6-13-23 To Do: Add code check algo. Print to OLED 

SCK = machine.Pin(2)
MOSI = machine.Pin(3)
RES = machine.Pin(29)
DC = machine.Pin(28)
CS = machine.Pin(27)

R1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
R2 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)
R3 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
R4 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)

C1 = machine.Pin(20, machine.Pin.OUT)
C2 = machine.Pin(21, machine.Pin.OUT)
C3 = machine.Pin(22, machine.Pin.OUT)

OLED = machine.SPI(0, baudrate=400000, sck=SCK, mosi = MOSI)
disp = SSD1306_SPI(width=128,height=64,spi=OLED,dc=DC,res=RES,cs=CS)

#disp.text("1",0,32)
#disp.text("2",10,32)
#disp.show()

debounce_time = 200
pinCode = [1,4,4,9,6,5]
code = []
code.clear()
count = 0
def enter_pressed():
    print(code)
    for i in code:
        print(i)
    
    

while True:
    C1.value(1)
    if (R1.value() and count<7):
        #print(count)
        #disp.text("7",0+(10*count),32)
        code.append(7)
        disp.text(code,0+(10*count),32)
        disp.show()
        
        time.sleep_ms(debounce_time)
        count = count+1
    if R2.value():
        #print("4")
        code.append(4)
        time.sleep_ms(debounce_time)
    if R3.value():
        #print("1")
        code.append(1)
        time.sleep_ms(debounce_time)
    if R4.value():
        print("CLEAR")
        code.clear()
        time.sleep_ms(debounce_time)
    C1.value(0)
    C2.value(1)
    if R1.value():
        #print("8")
        code.append(8)
        time.sleep_ms(debounce_time)
    if R2.value():
        #print("5")
        code.append(5)
        time.sleep_ms(debounce_time)
    if R3.value():
        #print("2")
        code.append(2)
        time.sleep_ms(debounce_time)
    if R4.value():
        #print("0")
        code.append(0)
        time.sleep_ms(debounce_time)
    C2.value(0)
    C3.value(1)
    if R1.value():
        #print("9")
        code.append(9)
        time.sleep_ms(debounce_time)
    if R2.value():
        #print("6")
        code.append(6)
        time.sleep_ms(debounce_time)
    if R3.value():
        #print("3")
        code.append(3)
        time.sleep_ms(debounce_time)
    if R4.value():
        #print("Enter")
        enter_pressed()
        time.sleep_ms(debounce_time)
    C3.value(0)

