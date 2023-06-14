import machine
import time
from ssd1306 import SSD1306_I2C



R1 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
R2 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
R3 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
R4 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)

C1 = machine.Pin(6, machine.Pin.OUT)
C2 = machine.Pin(7, machine.Pin.OUT)
C3 = machine.Pin(8, machine.Pin.OUT)

while True:
    C1.value(1)
    if R1.value():
        print("1")
        time.sleep_ms(250)
    if R2.value():
        print("4")
        time.sleep_ms(250)
    if R3.value():
        print("7")
        time.sleep_ms(250)
    if R4.value():
        print("CLEAR")
        time.sleep_ms(250)
    C1.value(0)
    C2.value(1)
    if R1.value():
        print("2")
        time.sleep_ms(250)
    if R2.value():
        print("5")
        time.sleep_ms(250)
    if R3.value():
        print("8")
        time.sleep_ms(250)
    if R4.value():
        print("0")
        time.sleep_ms(250)
    C2.value(0)
    C3.value(1)
    if R1.value():
        print("3")
        time.sleep_ms(250)
    if R2.value():
        print("6")
        time.sleep_ms(250)
    if R3.value():
        print("9")
        time.sleep_ms(250)
    if R4.value():
        print("Enter")
        time.sleep_ms(250)
    C3.value(0)
