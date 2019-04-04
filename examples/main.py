from microbit import *
from SW10 import SW10

SW10 = SW10()

while True:
    temp = SW10.readTempC()
    display.scroll(temp)
    sleep(1000)
