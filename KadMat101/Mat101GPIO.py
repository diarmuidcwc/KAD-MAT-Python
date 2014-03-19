from ctypes import *

class Mat101GPIO():

    def __init__(self):
        cdll.LoadLibrary("libmat101.so.1")
        self.libmat101 = CDLL("libmat101.so.1")

        try:
            self.libmat101.mat101_init()
        except:
            raise Exception

        self.BankDirection = ["OUT","OUT"]


    def ConfigureBankDirection(self):
        DirToHW = {"OUT" : 0, "IN" : 1}
        try:
            self.libmat101.mat101_gpio_setDir(DirToHW[self.BankDirection[0]],DirToHW[self.BankDirection[1]])
        except:
            raise Exception("Failed to set BankDirection ")


    def WriteToGPIO(self,data):
        try:
            data_char = c_ubyte(data)
        except:
            raise Exception ("Cannot convert input to 8 bit character")
        self.libmat101.mat101_gpio_set(data_char)



    def SetGPIOPint(self,PinNumber,OnNotOff):

        current_state = c_ubyte()
        self.libmat101.mat101_gpio_get(byref(current_state))

        gpio_change = 0 # Default to switch off the pin
        if OnNotOff == True:
            gpio_change = pow(2,PinNumber)

        set_state = c_ubyte( current_state.value | gpio_change)
        self.libmat101.mat101_gpio_set(set_state)



    def CloseGPIO(self):
        self.libmat101.mat101_exit()
