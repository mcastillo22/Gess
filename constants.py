SLEET = ( 79,  93, 115)
HL    = (255, 255, 200)
WHITE = (255, 255, 255)
GREY  = (128, 128, 128)

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