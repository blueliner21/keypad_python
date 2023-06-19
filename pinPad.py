SCK = machine.Pin(2)
MOSI = machine.Pin(3)
CS = machine.Pin(0, machine.Pin.OUT)

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