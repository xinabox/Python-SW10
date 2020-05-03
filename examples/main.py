from xSW10 import xSW10
from xCore import xCore

SW10 = xSW10()

while True:
    temp = SW10.readTempC()
    print(temp)
    xCore.sleep(1000)
