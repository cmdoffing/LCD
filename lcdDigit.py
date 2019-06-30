import copy

class LcdDigit():
    """
    The chief problem lies in storing the figures so that each can be expanded
    to any size (1 <= s <= 10). This will be done by storing the LCD
    represenation with s == 1. When I need to scale it, I will just multiply
    each of the characters.
    When scaling horizontally, only the blanks and the dashes get mulltiplied.
    The pipe chars are left as is.
    A key concept is that of "verticalOnly row". These contain only pipes and
    blanks. These are easy to scale because you can just multiply the list.
    The list should already be horizontally scaled.
    Horizontal lines should just get the dash or the middle blank multipled.
    A horizontal scale only scales one dash or the middle blank. 
    If there is a dash, no blank is scaled.
    If a row has only blanks and pipes, then only the middle blank is scaled.

    Horizontal Invariants:
    * An all blank row get only additive blanks.
    * A row with one or more pipes gets only blanks in the middle.
    * A row with dashes gets a total of additive more dashes.
    * All dashes are added in the middle.
    
    Vertical Invariants:
    * Vertical changes happen only after all horiz changes are complete.
    * Dash rows do not gete replicated but are left as the horiz change
      has left them.
    * Blank rows are also not replicated, just like dash rows.
    * Pipe rows are copied additive times.
    """

    figures = [
        [[' ', '-', ' '],   # 0
         ['|', ' ', '|'],
         [' ', ' ', ' '],
         ['|', ' ', '|'],
         [' ', '-', ' ']],

        [[' ', ' ', ' '],   # 1
         [' ', ' ', '|'],
         [' ', ' ', ' '],
         [' ', ' ', '|'],
         [' ', ' ', ' ']],

        [[' ', '-', ' '],   # 2
         [' ', ' ', '|'],
         [' ', '-', ' '],
         ['|', ' ', ' '],
         [' ', '-', ' ']],

        [[' ', '-', ' '],   # 3
         [' ', ' ', '|'],
         [' ', '-', ' '],
         [' ', ' ', '|'],
         [' ', '-', ' ']],

        [[' ', ' ', ' '],   # 4
         ['|', ' ', '|'],
         [' ', '-', ' '],
         [' ', ' ', '|'],
         [' ', ' ', ' ']],

        [[' ', '-', ' '],   # 5
         ['|', ' ', ' '],
         [' ', '-', ' '],
         [' ', ' ', '|'],
         [' ', '-', ' ']],

        [[' ', '-', ' '],   # 6
         ['|', ' ', ' '],
         [' ', '-', ' '],
         ['|', ' ', '|'],
         [' ', '-', ' ']],

        [[' ', '-', ' '],   # 7
         [' ', ' ', '|'],
         [' ', ' ', ' '],
         [' ', ' ', '|'],
         [' ', ' ', ' ']],

        [[' ', '-', ' '],   # 8
         ['|', ' ', '|'],
         [' ', '-', ' '],
         ['|', ' ', '|'],
         [' ', '-', ' ']],

        [[' ', '-', ' '],   # 9
         ['|', ' ', '|'],
         [' ', '-', ' '],
         [' ', ' ', '|'],
         [' ', '-', ' ']],
    ]

    def __init__(self, character, scale ):
        self.scale = scale
        self.additive = self.scale - 1
        self.char  = character
        self.digit = int( self.char )
        self.fig = self.figures[ self.digit ]
        self.template = copy.deepcopy( self.fig )
        self.scaleHoriz()
        self.scaleVert()

    def isBlankRow(self, row):
        return row[0] == row[1] == row[2] == ' '

    def insertBlanks(self, row):
        """ Use this to insert blanks in blank rows and pipe rows """
        for i in range(self.additive):
            row.insert(1, ' ')

    def isPipeRow(self, row):
        return row[0] == '|' or row[2] == '|'

    def isDashRow(self, row):
        return row[1] == '-'

    def insertDashes(self, row):
        for i in range(self.additive):
            row.insert(1, '-')

    def scaleHoriz(self):
        for row in self.template:
            #row.append( ' ' )
            if self.isBlankRow( row ) or self.isPipeRow( row ):
                self.insertBlanks( row )
            elif self.isDashRow( row ):
                self.insertDashes( row )
            else:
                print( "Programmer error in scaleHoriz" )

    def scaleVert(self):
        row3 = self.template[3]
        for i in range(self.additive):
            self.template.insert( 3, row3 )
        row1 = self.template[1]
        for i in range(self.additive):
            self.template.insert( 1, row1 )
