from microbit import i2c

SW10_ADDR = 0x4B
LM75B_REG_TEMP = 0x00

class SW10:
    
    def __init__(self, addr=SW10_ADDR):
        self.addr = addr
        
    def readTempC(self):
        i2c.write(self.addr, str(LM75B_REG_TEMP))
        data = i2c.read(self.addr, 2)
        tempC = (data[0] * 256 + data[1])/32 * 0.125
        return tempC
