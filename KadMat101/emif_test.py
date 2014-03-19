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

import Mat101Emif as emif

def main():
    myemif = emif.Mat101Emif()
    myemif.GetBuffer()

if __name__ == '__main__':
    main()
