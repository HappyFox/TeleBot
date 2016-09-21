upload: 
	ampy put adafruit/__init__.py 
	ampy put adafruit/pca9685.py 
	ampy put adafruit/i2cutils.py
	ampy put adafruit/main.py 

ls:
	ampy ls

test: upload
	ampy run test.py

repl:
	picocom /dev/tty.SLAB_USBtoUART -b 115200
