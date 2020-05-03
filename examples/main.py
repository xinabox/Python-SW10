from xSW10 import xSW10

SW10 = xSW10()

while True:
    temp = SW10.readTempC()
    print(temp)
    sleep(1000)
