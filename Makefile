upload: 
	ampy put drivers/__init__.py drivers/__init__.py 
	ampy put drivers/pca9685.py drivers/pca9685.py 
	ampy put drivers/i2cutils.py drivers/i2cutils.py
	ampy put drivers/adafruit/__init__.py drivers/adafruit/__init__.py
	ampy put drivers/adafruit/motorshield.py drivers/adafruit/motorshield.py
	ampy put drivers/bno055.py drivers/bno055.py
	ampy put main.py 

ls:
	ampy ls

setup:
	ampy mkdir drivers
	ampy mkdir drivers/adafruit

test: upload
	ampy run test.py

repl:
	picocom /dev/tty.SLAB_USBtoUART -b 115200
