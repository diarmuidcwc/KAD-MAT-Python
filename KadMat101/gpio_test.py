#-------------------------------------------------------------------------------
# Name:        gpio_test
# Purpose:     Example script that toggles the GPIO pins on the KAD/MAT/101
#
# Author:      DCollins
#
# Created:     19/03/2014
#
# Copyright 2014 Diarmuid Collins
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------


import sys
import Mat101GPIO as gpio
import time


def main():
    mygpio = gpio.Mat101GPIO()

    # Swich off all pins
    mygpio.WriteToGPIO(0)
    time.sleep(1)

    # Now switch on the pins one by one
    print "Switching on the pins one by one"
    for count in xrange(8):
        mygpio.SetPin(count,True);
        time.sleep(1)

    print "Switching off the pins one by one"
    for count in xrange(8):
        mygpio.SetPin(count,False);
        time.sleep(1)

    mygpio.CloseGPIO()
    exit()

if __name__ == '__main__':
    main()
