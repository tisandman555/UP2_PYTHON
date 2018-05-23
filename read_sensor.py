import time
from upm import pyupm_th02 as grove
import mraa

mraa.addSubplatform(mraa.GROVEPI, "0") 

def main():
    th02 = grove.TH02()
    print(th02.name())
    # Create the temperature sensor object using AIO pin 0
    temp = th02.getTemperature()
    print(temp)

    # Read the temperature ten times, printing both the Celsius and
    # equivalent Fahrenheit temperature, waiting one second between readings
    for i in range(0, 1000):
        temp = th02.getTemperature()
        temp1 = th02.getHumidity()
        print(temp, temp1)
        time.sleep(1)

    # Delete the temperature sensor object
    del temp

if __name__ == '__main__':
    main()
