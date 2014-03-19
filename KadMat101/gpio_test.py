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


    for count in xrange(100):
        data = count % 0x100
        mygpio.WriteToGPIO(data)
        time.sleep(1)


    mygpio.CloseGPIO()
    exit()

if __name__ == '__main__':
    main()
