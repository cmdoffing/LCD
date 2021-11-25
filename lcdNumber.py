from lcdDigit import LcdDigit

class LcdNumber():

    def __init__(self, scale, numString):
        self.lcdString = numString
        self.scale     = scale
        self.digits    = list( numString )
        self.numDigits = len( self.digits )
        self.display   = []
        for digit in self.digits:
            self.display.append( LcdDigit(digit, self.scale).template )

    def lcdDisplay(self):
        """
        Concat      display[0][0] with display[1][0].
        Then concat display[0][1] with display[1][1].
        Then concat display[0][2] with display[1][2].
        Etc. The last index is on the height and the first is over the
        self.dislpay structure. Note that the first index (numDigits) 
        is inside the second index and so the loop structure is inverted.
        Each low level list is treated as a unit and not indexed into, which
        means that it is largely irrelevant that it is a list.
        """
        height = self.scale * 2 + 3        
        lcdList = []
        for i in range( height ):
            dn = []
            for digit in self.display:
                dn += digit[i] + [' ']
            lcdList += dn + ['\n']
        return lcdList

