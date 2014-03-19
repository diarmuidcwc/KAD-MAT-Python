#-------------------------------------------------------------------------------
# Name:        Mat101GPIO
# Purpose:     Class to manage the GPIO interface on the KAD/MAT/101 from Python
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

from ctypes import *

class Mat101GPIO():
    '''Class to control the GPIO pins on the top block of the KAD/MAT/101'''
    def __init__(self):
        cdll.LoadLibrary("libmat101.so.1")
        self.libmat101 = CDLL("libmat101.so.1")

        try:
            self.libmat101.mat101_init()
        except:
            raise Exception

        self.BankDirection = ["OUT","OUT"]


    def SetBankDirection(self):
        '''Set the direction of the GPIO banks'''
        DirToHW = {"OUT" : 0, "IN" : 1}
        try:
            self.libmat101.mat101_gpio_setDir(DirToHW[self.BankDirection[0]],DirToHW[self.BankDirection[1]])
        except:
            raise Exception("Failed to set BankDirection ")


    def WriteToGPIO(self,data):
        '''Write a byte to the GPIO controlling the pins. Reversed order. One bit per pin'''
        try:
            data_char = c_ubyte(data)
        except:
            raise Exception ("Cannot convert input to 8 bit character")
        self.libmat101.mat101_gpio_set(data_char)



    def SetPin(self,PinNumber=0,OnNotOff=False):
        '''Drive one particular GPIO pin. Can be switched on or off'''

        current_state = c_ubyte() # To store the read back value of the current gpio state
        self.libmat101.mat101_gpio_get(byref(current_state))

        gpio_change = pow(2,7-PinNumber) # Find the pin we want to change 
        if OnNotOff == True:
            set_state = c_ubyte( current_state.value | gpio_change)
	else:
            set_state = c_ubyte( current_state.value &  ~gpio_change)

        self.libmat101.mat101_gpio_set(set_state)



    def CloseGPIO(self):
        '''Close the GPIO and free up the program memory'''
        self.libmat101.mat101_exit()
