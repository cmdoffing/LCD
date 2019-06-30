# This program displays LCD digits, given a command line size 
# parameter (s = param 1) and a number to display (param 2).
# Let s be the number of horizontal segments, then each LCD digit will
# occupy s + 2 positions and 2s + 3 vertical rows.
# There must be one column of blanks between two digits.
# This file handles the command line interface.
# Sample input line:   lcd.py 2 12345

from lcdNumber import LcdNumber
import sys

lcdNum = LcdNumber( int( sys.argv[1]), sys.argv[2] )
displayDigits = lcdNum.lcdDisplay()
print( ''.join( displayDigits ))
