import turtle
from turtle import Screen, Turtle

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.tracer(0, 0)
turtle.hideturtle()

def draw_board():
    turtle.pencolor('black')
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3, -1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3, 1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1, -3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1, -3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)


def draw_circle(x, y):
    turtle.up()
    turtle.goto(x, y - 0.75)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.circle(0.75, steps=100)


def draw_x(x, y):
    turtle.color('blue')
    turtle.up()
    turtle.goto(x - 0.75, y - 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y + 0.75)
    turtle.up()
    turtle.goto(x - 0.75, y + 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y - 0.75)


def draw_piece(i, j, p):
    if p == 0: return
    x, y = 2 * (j - 1), -2 * (i - 1)
    if p == 1:
        draw_x(x, y)
    else:
        draw_circle(x, y)


def draw(b):
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i, j, b[i][j])
    screen.update()


# return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
def gameover(b):
    if b[0][0] > 0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]:
        return b[0][0]
    if b[1][0] > 0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]:
        return b[1][0]
    if b[2][0] > 0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]:
        return b[2][0]
    if b[0][0] > 0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]:
        return b[0][0]
    if b[0][1] > 0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]:
        return b[0][1]
    if b[0][2] > 0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]:
        return b[0][2]
    if b[0][0] > 0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        return b[0][0]
    if b[2][0] > 0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]:
        return b[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p == 9: return 3
    else: return 0


def play(x, y):
    global turn
    i = 3 - int(y + 5) // 2
    j = int(x + 5) // 2 - 1
    if i > 2 or j > 2 or i < 0 or j < 0 or b[i][j] != 0: return
    if turn == 'x': b[i][j], turn = 1, 'o'
    else: b[i][j], turn = 2, 'x'
    draw(b)
    r = gameover(b)
    if r == 1:
      turtle.setpos(0,-5)
      turtle.write("Game over! X won!", align = "center", font=("Calibri", 40, "bold"))
      return
    elif r == 2:
      turtle.setpos(0,-5)
      turtle.write("Game over! O won!", align = "center", font=("Calibri", 40, "bold"))
      return
    elif r == 3:
      turtle.setpos(0,-5)
      turtle.write("Game over! Tie!", align = "center", font=("Calibri", 40, "bold"))
      return




def start():
  b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  draw(b)
  turn = 'x'
  screen.onclick(play)
  turtle.mainloop()

#https://pythontpoint.in/python-turtle-play-tic-tac-toe/#:~:text=The%20Python%20turtle%20Play%20Tic%20Tac%20Toe%20is%20a%20game,with%20three%200's%20or%20x's.

CURSOR_SIZE = 20
FONT_SIZE = 30
FONT = ('Arial', FONT_SIZE, 'bold')

button = Turtle()
button.hideturtle()
screen.register_shape('play.gif')
button.shape('play.gif')
button.penup()
button.goto(0, -70)
button.write("PLAY TIC TAC TOE", align='center', font=FONT)
button.sety(0 + CURSOR_SIZE + FONT_SIZE)
button.onclick(start)
button.showturtle()

turtle = Turtle()
turtle.hideturtle()

screen = Screen()
screen.mainloop()
