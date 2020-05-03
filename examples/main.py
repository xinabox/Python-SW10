from microbit import *
from xSW10 import xSW10

xSW10 = xSW10()

while True:
    temp = xSW10.readTempC()
    display.scroll(temp)
    sleep(1000)
