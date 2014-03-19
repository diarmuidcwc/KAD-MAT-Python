#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DCollins
#
# Created:     19/03/2014
# Copyright:   (c) DCollins 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import Mat101GPIO as gpio
import time


def main():
    mygpio = gpio.Mat101GPIO()

    mygpio.BankDirection[0] = "OUT"
    mygpio.BankDirection[1] = "OUT"

    mygpio.ConfigureBankDirection()


    for count in xrange(50):
        data = count % 0x100
	print "Writing {:8b}".format(data)
        mygpio.WriteToGPIO(data)
        time.sleep(1)

    mygpio.WriteToGPIO(0)
    time.sleep(1)
    print "Switching on the pins one by one"
    for count in xrange(8):
        mygpio.SetGPIOPin(count,True);
        time.sleep(1)

    for count in xrange(8):
        mygpio.SetGPIOPin(count,False);
        time.sleep(1)

    mygpio.CloseGPIO()
    exit()

if __name__ == '__main__':
    main()
