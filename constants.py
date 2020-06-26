# Game colors
SLEET       = ( 79,  93, 115)
HL          = (255, 255, 200)
WHITECOLOR  = (255, 255, 255)
GREY        = (128, 128, 128)

# Sizes
WINDOW_SIZE = (700, 700)
ARRAY = 20
SPACE = 30
PIECE = SPACE * 3
BUTTON_SIZE = 25

# Coordinates
X1, Y1 = 50, 50
PIECE_POS = X1 + 3

TURN_SPACE = int(X1 + SPACE*7.5)
TURN_HEIGHT = int(SPACE*0.45)

NEW_GAME_X = int(X1 + SPACE*15.5)

WINNER = X1 + SPACE*5, Y1 + SPACE*7

# Board Array
BOARD_ARRAY = [x for x in range(X1, (ARRAY+1)*SPACE, SPACE)]

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
