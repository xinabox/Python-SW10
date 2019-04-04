# Write your code here :-)
from microbit import *
import SW10

while True:
    temp = SW10.readTempC()
    display.scroll(temp)
    sleep(2000)