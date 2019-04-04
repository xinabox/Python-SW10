from microbit import i2c

class SW10:
	def readTempC():
    	i2c.write(SW10_ADDR, str(LM75B_REG_TEMP))
    	data = i2c.read(SW10_ADDR, 2)
    	tempC = (data[0] * 256 + data[1])/32 *0.125
    	return tempC