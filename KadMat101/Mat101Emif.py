from Mat101Shared import *


class Mat101Emif():
    def __init__(self):

        cdll.LoadLibrary("libmat101.so.1")
        self.libmat101 = CDLL("libmat101.so.1")

        try:
            self.libmat101.mat101_init()
        except:
            raise Exception
        self.currentbuffer = m101_userBuffer_h()


    def GetBuffer(self):
        try:
            self.libmat101.mat101_get_buffer(self.currentbuffer)
        except:
            raise Exception("Failed to get a buffer")
