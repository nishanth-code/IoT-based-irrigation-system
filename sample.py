import machine
import time

# Define the GPIO pin connected to the relay module
relay_pin = machine.Pin(15, machine.Pin.OUT)

# Function to toggle the relay ON or OFF
def waterpump_on():
    relay_pin.on()
def waterpump_off():
    relay_pin.off()
    
waterpump_off()
    


    

