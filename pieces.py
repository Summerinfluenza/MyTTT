from turtle import Turtle

POSITIONS = {"1": (-200, 200),
             "2": (0, 200),
             "3": (200, 200),
             "4": (-200, 0),
             "5": (0, 0),
             "6": (200, 0),
             "7": (-200, -200),
             "8": (0, -200),
             "9": (200, -200),
             }


class Piece:
    def __init__(self):
        self.player = "player"
        self.computer = "computer"

    def create_piece(self, position, side):
        if side == self.player:
            new_piece = Turtle()
            new_piece.hideturtle()
            new_piece.penup()
            new_piece.color("white")
            new_piece.pensize(15)
            new_piece.goto(POSITIONS[position])
            new_piece.forward(80)
            new_piece.setheading(90)
            new_piece.pendown()
            new_piece.circle(80)

        elif side == self.computer:
            new_piece = Turtle()
            new_piece.hideturtle()
            new_piece.penup()
            new_piece.color("white")
            new_piece.pensize(15)
            new_piece.goto(POSITIONS[position])
            new_piece.setheading(45)
            new_piece.forward(80)
            new_piece.pendown()
            new_piece.backward(160)
            new_piece.penup()
            new_piece.goto(POSITIONS[position])
            new_piece.setheading(135)
            new_piece.forward(80)
            new_piece.pendown()
            new_piece.backward(160)
