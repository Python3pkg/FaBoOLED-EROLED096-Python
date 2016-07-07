# coding: utf-8
## @package FaBoOLED_EROLED096
#  This is a library for the FaBo OLED I2C Brick.
#
#  http://fabo.io/214.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoOLED_EROLED096
import time

oled = FaBoOLED_EROLED096.EROLED096()

time.sleep(1)
oled.clear()

oled.showBitmap()

time.sleep(1)
oled.clear()
time.sleep(1)

oled.write("* OLED SAMPLE *")

i = 0

while True:
    oled.setCursor(0,1)
    oled.write("--OUTPUT DATA--")

    oled.setCursor(1,2)
    oled.write("I :")
    oled.write(i)

    oled.setCursor(1,3)
    oled.write("I/10:")
    oled.write(i*0.1)

    oled.setCursor(0,4)
    oled.write("--OUTPUT LIST--")

    oled.setCursor(1,5)
    oled.write(["BIN:", str(bin(i))])

    oled.setCursor(1,6)
    oled.write(["HEX:", str(hex(i))])

    time.sleep(1)
    i += 1
