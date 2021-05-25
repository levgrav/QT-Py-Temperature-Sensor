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

You will see a new disk drive appear called QTPY_BOOT.

<img src="https://github.com/levgrav/QT-Py-Temperature-Sensor/blob/main/images/QTPY_BOOT.png" width=50% height=50%>

Drag the adafruit_circuitpython_etc.uf2 file to QTPY_BOOT. The red LED will flash. Then, the QTPY_BOOT drive will disappear and a new disk drive called CIRCUITPY will appear.

That's it, you're done! :)

## The Circuit
