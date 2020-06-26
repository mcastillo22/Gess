# Game colors
SLEET = ( 79,  93, 115)
HL    = (255, 255, 200)
WHITE = (255, 255, 255)
GREY  = (128, 128, 128)

# Coordinates
WINDOW_SIZE = (700, 700)
ARRAY = 20
SPACE = 30

X1, Y1 = 50, 50
PIECE = SPACE * 3
PIECE_POS = X1 + 3

TURN_SPACE = int(X1 + SPACE*7.5)
TURN_HEIGHT = int(SPACE*0.45)

BOARD_ARRAY = [x for x in range(X1, (ARRAY+1)*SPACE, SPACE)]

WINNER = X1 + SPACE*5, Y1 + SPACE*7

# Strings
TITLE = 'Gess Game'

BLACK = 'BLACK'
WHITE = 'WHITE'
B = 'B'
W = 'W'

UNFINISHED  = 'UNFINISHED'
BLACK_WON   = 'BLACK_WON'
WHITE_WON   = 'WHITE_WON'

ALPHA = 'abcdefghijklmnopqrst'

SW      = 'SW'
S       = 'S'
SE      = 'SE'
W       = 'W'
CENTER  = 'Center'
E       = 'E'
NW      = 'NW'
N       = 'N'
NE      = 'NE'

