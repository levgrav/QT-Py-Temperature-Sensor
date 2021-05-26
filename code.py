import board # necessary for anything using the pins
import adafruit_ssd1306              ''' *** for display w/out chip *** '''
import time
from digitalio import DigitalInOut, Direction # for leds (on and off)
from analogio import AnalogIn # for thermistor reading
import math

calcA = 0.03877     # numbers for later calculations DO NOT USE THESE THEY WILL NOT WORK FOR YOURS
calcB = 1.038836108

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)  # width, height, i2c obj

blueLed = DigitalInOut(board.D1)    # Defining pins for leds
greenLed = DigitalInOut(board.D2)
redLed = DigitalInOut(board.D3)

blueLed.direction = Direction.OUTPUT  # defining directions
greenLed.direction = Direction.OUTPUT
redLed.direction = Direction.OUTPUT

blueLed.value = 0    # making sure they are all off
greenLed.value = 0
redLed.value = 0

therm = AnalogIn(board.A0) # defining the thermistor pin
#time.sleep (0.1)

def get_voltage(pin):
    
    volts = (pin.value * 3.3) / 65536 # official calculation from adafruit
    time.sleep(0.1)
    return volts

def get_temp(voltage):
    calc1 = 3.3 - voltage    # My equation for the graph        *** DO NOT USE IT WILL NOT WORK ***
    calc2 = calc1 / calcA
    calc3 = math.log(calc2)
    calc4 = math.log(calcB)
    calc5 = calc3 / calc4

    return calc5

def determineLED(temp):  
    if (temp >= 40):      # use whatever numbers for these you want (these are in degrees C)
        return redLed
    elif (temp < 25): 
        return blueLed
    else:
        return greenLed

while True:
    v = get_voltage(therm)  # finding voltage and temperature
    t = get_temp(v)

        ''' *** for display w/out chip *** '''
# +---------------------------------------------------+    
    oled.fill(0) # fill the display with black
    oled.text("Volts: " + str(round(v , 3)), 0,0,1 ) # displays text in the top left corner (0,0) that says "Volts: " and than the voltage rounded to 3 decimals 
    oled.text("Temp:  " + str(round(t , 1)), 0,20,1) # displays temp just under that (0, 20)
# +---------------------------------------------------+

    print("Volts:  " + str(round(v , 3)))
    print("Temp:  " + str(round(t , 1)))
    
    blueLed.value = 0
    greenLed.value = 0
    redLed.value = 0
    
    determineLED(t).value = 1
    
    time.sleep(0.1)
    
    oled.show() # activates the oled            *** for display w/out chip ***
