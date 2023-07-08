import machine
import time
import neopixel

SCK = machine.Pin(2)
MOSI = machine.Pin(3)
CS = machine.Pin(0, machine.Pin.OUT)

Green = [0,255,0]
Red = [255,0,0]
Blank = [0,0,0]

decode_mode = bytearray([0x09,0xFF])
intensity = bytearray([0x0A,0x0F])
scan_limit = bytearray([0x0B,0x07])
mode = bytearray([0x0C,0x01])
test = bytearray([0x08,0x07])

pinCode = [1,4,4,9,6,5]

SPI0=machine.SPI(0,baudrate=10000,sck=SCK,mosi=MOSI)
RGB = neopixel.NeoPixel(machine.Pin(8),1)
RGB[0] = Blank
RGB.write()
    

def display_init():
    CS.value(0)
    SPI0.write(decode_mode)
    CS.value(1)
    time.sleep_ms(10)
    
    CS.value(0)
    SPI0.write(intensity)
    CS.value(1)
    time.sleep_ms(10)
    
    CS.value(0)
    SPI0.write(scan_limit)
    CS.value(1)
    time.sleep_ms(10)
    
    CS.value(0)
    SPI0.write(mode)
    CS.value(1)
    time.sleep_ms(10)
    
    
    
    
        
def display_write(reg,buffer):
    CS.value(0)
    SPI0.write(bytearray([reg,buffer]))
    CS.value(1)
    time.sleep_ms(10)
    
def display_clear(num_digits):
    i=num_digits
    while(i>0):
        CS.value(0)
        SPI0.write(bytearray([i,0x0F]))
        CS.value(1)
        time.sleep_ms(10)
        i-=1

def enter_pressed(code):
    print(code)
    if (code == pinCode):
        print("Correct Code")
        RGB[0] = Green
        RGB.write()
         
    else:
        print("WRONG")
        RGB[0] = Red
        RGB.write()
    