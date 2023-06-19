import machine
import time
import pinPad

#Code 144965
R1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
R2 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)
R3 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
R4 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)

C1 = machine.Pin(20, machine.Pin.OUT)
C2 = machine.Pin(21, machine.Pin.OUT)
C3 = machine.Pin(22, machine.Pin.OUT)
  
debounce_time = 200
code = []
code.clear()
count = 7

pinPad.display_init()
pinPad.display_clear(8)
#pinPad.display_write(1,8)


while True:
    C1.value(1)
    if (R1.value() and count<=7 and count>=2):
        code.append(7)
        pinPad.display_write(count,7)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    elif (R2.value() and count<=7 and count>=2):
        code.append(4)
        pinPad.display_write(count,4)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    elif (R3.value() and count<=7 and count>=2):
        code.append(1)
        pinPad.display_write(count,1)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    elif (R4.value()):
        code.clear()
        pinPad.display_clear(8)
        time.sleep_ms(debounce_time)
        count=7
        print(count)
    C1.value(0)
    
    C2.value(1)
    if (R1.value() and count<=7 and count>=2):
        code.append(8)
        pinPad.display_write(count,8)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    elif (R2.value() and count<=7 and count>=2):
        code.append(5)
        pinPad.display_write(count,5)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    elif (R3.value() and count<=7 and count>=2):
        code.append(2)
        pinPad.display_write(count,2)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    elif (R4.value() and count<=7 and count>=2):
        code.append(0)
        pinPad.display_write(count,0)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    C2.value(0)
    
    C3.value(1)
    if (R1.value() and count<=7 and count>=2):
        code.append(9)
        pinPad.display_write(count,9)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    elif (R2.value() and count<=7 and count>=2):
        code.append(6)
        pinPad.display_write(count,6)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    elif (R3.value() and count<=7 and count>=2):
        code.append(3)
        pinPad.display_write(count,3)
        time.sleep_ms(debounce_time)
        count-=1
        print(count)
    elif (R4.value()):
        pinPad.enter_pressed(code)
        time.sleep_ms(debounce_time)
        count=7
        print(count)
        pinPad.display_clear(8)
        code.clear()
    C3.value(0)
    
    
 
   

