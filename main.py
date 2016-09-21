from machine import Pin, I2C

import pca9685

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

pca = pca9685.Pca9685(i2c, 0x60)
pca.freq(1600)

eight = pca9685.Pwm(pca, 8)
nine = pca9685.Pin(pca, 9)
ten = pca9685.Pin(pca, 10)
