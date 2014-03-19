from ctypes import *

class Mat101GPIO(self):

    GPIO_DIR_OUTPUT = 0
    GPIO_DIR_INPUT = 1

    def __init__(self):
        cdll.LoadLibrary("libmat101.so.1")
        self.libmat101 = CDLL("libmat101.so.1")

        try:
            self.libmat101.mat101_init
        except:
            raise Exception

        self.Bank1Direction = "out"
        self.Bank2Direction = "out"
