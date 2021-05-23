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
	
## Setup / Prerequisite installations
Follow these instructions to set up you QT Py or go to the following link: https://learn.adafruit.com/adafruit-qt-py/overview

To start, go to https://circuitpython.org/board/qtpy_m0/ to download the latest version of CircuitPython.

Download and save it to your desktop (or wherever is handy).

Plug your QT Py into your computer using a known-good USB cable.

#### A lot of people end up using charge-only USB cables and it is very frustrating! So make sure you have a USB cable you know is good for data sync.

Double-click the small RST (reset) button, and you will see the NeoPixel RGB LED turn green. If it turns red, check the USB cable, try another USB port, etc.
![QT_Py_Neopixel_Green](./images/QT_Py_Neopixel_green.jpg)
If double-clicking doesn't work the first time, try again. Sometimes it can take a few tries to get the rhythm right!
