import machine
import time



def read_soilmoistureDigital():
    moisture_digital_pin = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
    moisture_level = moisture_digital_pin.value()
    if moisture_level == 0:
        return 1
    else:
        return 0
def read_soilmoistureAnalog():
    moisture_digital_pin = machine.ADC(27)
    moisture_level = moisture_digital_pin.read_u16()
    return(moisture_level)
    
   
    


