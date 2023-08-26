import random
import turtle
import time

from random import randint

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("#4FC0D0")
turtle_screen.title("Catch The Turtle")
turtle_screen.setup(800,600)

finish_game=False

finisher_turtle=turtle.Turtle()
finisher_turtle.hideturtle()


turtle_object=turtle.Turtle()
turtle_object.hideturtle()
turtle_object.shapesize(stretch_len=2,stretch_wid=2)
turtle_object.color("green")
turtle_object.shape("turtle")
turtle_object.speed("slow")


FONT = ('Arial', 24, 'normal')
turtle_writer=turtle.Turtle()
score=0

def score_turtle():

    turtle_writer.hideturtle()
    turtle_writer.color("#164B60")
    turtle_writer.penup()
    y=(turtle_screen.window_height()-24)/2
    turtle_writer.setpos(0,y*0.9)
    turtle_writer.write(arg="Score: 0",move=False,align="center",font=FONT)

def random_move():
    if not finish_game:
        turtle_object.penup()
        turtle_object.hideturtle()

        def handle_click(x,y):
            global score
            turtle_writer.clear()
            score += 1
            turtle_writer.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)

        turtle_object.onclick(handle_click)
        turtle_object.goto(randint(-200,200),randint(-250,220))
        turtle_object.showturtle()
        turtle_screen.ontimer(random_move,750)
        time.sleep(0.3)
        turtle_object.hideturtle()


def finisher(time):
    global finish_game
    finisher_turtle.color("#BB2525")
    finisher_turtle.penup()
    y = (turtle_screen.window_height() - 100) / 2
    finisher_turtle.setpos(0, y * 0.9)

    if time>0:
        finisher_turtle.clear()
        finisher_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        turtle_screen.ontimer(lambda: finisher(time-1),1000)
    else:
        finish_game = True
        finisher_turtle.clear()
        finisher_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)
        turtle_object.hideturtle()


score_turtle()
random_move()
finisher(5)


turtle.mainloop()