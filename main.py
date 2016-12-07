from machine import Pin, I2C

from drivers.bno055 import Bno055
from drivers.adafruit import motorshield
from drivers.i2cutils import I2cRegDevice

BNO_CALIB_DATA = (b'\xf8\xff\x08\x00\x12\x00\xb4\xfe\xc5\xffU\x00\xfe\xff\x00'
                  b'\x00\x01\x00\xe8\x03c')

i2c = I2C(scl=Pin(5), sda=Pin(4), timeout=10000)

bno = Bno055(i2c, calib_data=BNO_CALIB_DATA)

shield = motorshield.get_motor_shield(i2c)
motor0 = shield.get_motor(0)
motor1 = shield.get_motor(1)
motor1.invert = True



# pca = pca9685.Pca9685(i2c, 0x60)
# pca.freq(1600)

# eight = pca9685.Pwm(pca, 8)
# nine = pca9685.Pin(pca, 9)
# ten = pca9685.Pin(pca, 10)

# eight = pca.init_pwm(8)
# nine = pca.init_pin(9)
# ten = pca.init_pin(10)
