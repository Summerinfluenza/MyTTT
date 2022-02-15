from turtle import Screen
from pieces import Piece
from board import Board

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.title("Tick Tack Toe")

piece = Piece()
board = Board()

board.create_board()
used_blocks = {}
next_turn = "o"


def move_piece(turn, block):
    global next_turn
    global used_blocks
    # To check if the block is occupied
    # To check whose turn
    if block not in used_blocks:
        if turn == "o":
            piece.create_piece(block, "player")
            used_blocks[block] = 1
            next_turn = "x"
        elif turn == "x":
            piece.create_piece(block, "computer")
            used_blocks[block] = 4
            next_turn = "o"


def blocks(x, y):
    global next_turn
    block = "0"

    # To check the block
    if y >= 100:
        if x <= -100:
            block = "1"
        elif -100 < x <= 100:
            block = "2"
        elif x > 100:
            block = "3"
    elif 100 > y >= -100:
        if x <= -100:
            block = "4"
        elif -100 < x <= 100:
            block = "5"
        elif x > 100:
            block = "6"
    elif y < -100:
        if x <= -100:
            block = "7"
        elif -100 < x <= 100:
            block = "8"
        elif x > 100:
            block = "9"

    move_piece(next_turn, block)
    screen.update()
    print(next_turn)


screen.onscreenclick(blocks)
screen.update()


screen.mainloop()
