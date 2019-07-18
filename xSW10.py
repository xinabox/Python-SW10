from xCore import xCore

LM75B_I2C_ADDR = 0x48
LM75B_REG_TEMP = 0x00

class xSW10:
    def __init__(self, addr=LM75B_I2C_ADDR):
        self.addr = addr
        self.i2c = xCore()

    def init(self):
        pass

    def getTempC(self):
        data = self.i2c.write_read(self.addr, LM75B_REG_TEMP, 2)
        tempC = (data[0] * 256 + data[1])/32 * 0.125
        return tempC

    def readTempF(self):
        return (1.8 * self.readTempC()) + 32
