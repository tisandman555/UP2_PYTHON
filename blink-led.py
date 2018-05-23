import mraa
import time

print(mraa.getVersion())

mraa.addSubplatform(mraa.GROVEPI, "0") 

gpio_4 = mraa.Gpio(512+4)

gpio_4.dir(mraa.DIR_OUT)

while True:
    gpio_4.write(1)
    time.sleep(1)
    gpio_4.write(0)
    time.sleep(1)



