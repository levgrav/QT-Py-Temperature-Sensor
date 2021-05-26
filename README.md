# QT Py DIY Temperature Sensor
Step-by-step instructions and code for a DIY temperature sensor using a QT Py with pictures
## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)

## Technologies
Project is created with:
* CircuitPython (6.1.0)

Parts:
* Adafruit QT Py (https://www.adafruit.com/product/4600)
* OLED Display (https://www.adafruit.com/product/4440) 
* STEMMA Cable (https://www.adafruit.com/product/4399)
* Thermistor (https://www.digikey.com/en/products/detail/vishay-beyschlag-draloric-bc-components/NTCLE100E3103JB0/769411)
* Breadborad
* LEDs (3; 1 red, 1 green, 1 blue)
* USB-C data cable
* 4x 330 ohm resistors
* 7x short jumper cables

Optional (for temperature probe)

* 4x long jumper cables
* Tape
* Heat shrink
* Hot glue (NOT RECOMENDED)
	
## Setup / Prerequisite installations
Follow these instructions to set up you QT Py or go to the following link: https://learn.adafruit.com/adafruit-qt-py/overview

To start, go to https://circuitpython.org/board/qtpy_m0/ to download the latest version of CircuitPython.

Download and save it to your desktop (or wherever is handy).

Plug your QT Py into your computer using a known-good USB cable.

#### A lot of people end up using charge-only USB cables and it is very frustrating! So make sure you have a USB cable you know is good for data sync.

Double-click the small RST (reset) button, and you will see the NeoPixel RGB LED turn green. If it turns red, check the USB cable, try another USB port, etc.

<img src="https://github.com/levgrav/QT-Py-Temperature-Sensor/blob/main/images/QT_Py_Neopixel_green.png" width=30% height=30%>

If double-clicking doesn't work the first time, try again. Sometimes it can take a few tries to get the rhythm right!

You will see a new disk drive appear called `QTPY_BOOT`.

<img src="https://github.com/levgrav/QT-Py-Temperature-Sensor/blob/main/images/QTPY_BOOT.png" width=50% height=50%>

Drag the `adafruit_circuitpython_etc.uf2` file to QTPY_BOOT. The red LED will flash. Then, the QTPY_BOOT drive will disappear and a new disk drive called `CIRCUITPY` will appear.

### Installing MU Editor (Highly seggested)

Mu is a simple code editor that works with the Adafruit CircuitPython boards. It's written in Python and works on Windows, MacOS, Linux and Raspberry Pi. The serial console is built right in so you get immediate feedback from your board's serial output!

if you already have a favorite IDE use that one because MU edotor is not the best IDE but it has the serial console built right in so at least use it for that.

### Programing your QT Py

Go into the IDE that you are using and create a python file in your CIRCUITPY directory. name the file `code.py` 

You can now program in python and you are going to have to google the special things you can do with this board because I am not writing it here.

My code: [code.py](code.py)

To run your code simply save it or hit the reset button. Any `print()` functions will show up on your serial console (in MU editor)

## The Circuit

<img src="https://github.com/levgrav/QT-Py-Temperature-Sensor/blob/main/images/circuit diagram.png">

## Setting up the OLED display

First thing you need to do is download this file onto any convenient folder (I just used my downloads folder).

[adafruit-circuitpython-bundle-6.x-mpy-20210321.zip](https://github.com/levgrav/QT-Py-Temperature-Sensor/files/6535930/adafruit-circuitpython-bundle-6.x-mpy-20210321.zip)

This is a ZIP file that contains many CircuitPython libraries, some of which we will need to copy onto the CIRCUITPY directory. Unzip the file.

### For people with the optional solderable flash chip:

For you it is very easy all you have to do is:

1. Go into the new folder that was just created when you unzipped the file
2. Go into the `lib` folder
3. Find `adafruit_displayio_ssd1306.mpy` and `adafruit_bus_device folders`
4. Copy them into the `lib` folder of your CIRCUITPY
5. Google ways to program it and copy in any aditional libraries called for 

### For the people without the optional solderable chip (What I had):

This is where it gets tricky and I had to do a lot of reaserch and trial and error. I can't find any source that actualy had a working  version of this, but I came up with this solution:

1. Go into the new folder that was just created when you unzipped the file
2. Go into the `lib` folder
3. Find the folder `adafruit_bus_device`
4. Copy that into the `lib` folder of your CIRCUITPY directory
5. Also find and copy `adafruit_framebuf.mpy` and `adafruit_ssd1306.mpy` into your lib folder
6. Next, go back the the unzipped folder and into `examples`
7. Find `font5x8.bin`
8. Copy this into your CIRCUITPY (outside the lib folder)

You will only be able to display text but the other libraries take too much space that you don't have because you don't have the optional flash chip.

My code (comments where there is something for the display): [code.py](code.py)

