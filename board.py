from turtle import Turtle

LINES_START = {"1": (-300, 100),
               "2": (-300, -100),
               "3": (-100, -300),
               "4": (100, -300)
               }

LINES_FINISH = {"1": (300, 100),
                "2": (300, -100),
                "3": (-100, 300),
                "4": (100, 300),
                }


class Board:
    def __init__(self):
        self.lines = 4

    def create_line(self, num):
        line = Turtle()
        line.hideturtle()
        line.penup()
        line.goto(LINES_START[str(num)])
        line.pencolor("green")
        line.pensize(20)
        line.pendown()
        line.goto(LINES_FINISH[str(num)])

    def create_board(self):
        for n in range(1, self.lines + 1):
            self.create_line(n)


board = Board()
print(board.lines)