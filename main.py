# Pong by Thuong Vo
# edited by MeisZy (9/11/22):
    #-added paddle collisions

import turtle, os, sys, math, random, time
from tkinter import *
 # Load the popular external library

#not used
def exit():
    wn.destroy()

wn = turtle.Screen()
wn.title("ping pong")
wn.bgcolor("#FFE5B4")
wn.setup(width = 800,height = 600)
wn.tracer(0)

os.system("cls")



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#mixer.init()
#mixer.music.load(resource_path('bounce.wav'))

# Objects
class Paddle:
    def __init__(self, x, y):
        """
        x -- starting x position \n
        y -- starting y position
        """
        self.obj = turtle.Turtle()
        self.obj.speed(0)
        self.obj.shape("square")
        self.obj.color("white")
        self.obj.shapesize(stretch_wid=5,stretch_len=1)
        self.obj.penup()
        self.obj.goto(x,y)
    def up(self):
        """Moves the paddle up"""
        y = self.obj.ycor()
        y += 20
        self.obj.sety(y)
    def down(self):
        """Moves the paddle down"""
        y = self.obj.ycor()
        y -= 20
        self.obj.sety(y)
    #bounce mechanic
    def bounce(self,Ball):
        minimum = self.size.x + Ball.radius
        if self.position.x != Ball.position.x and self.overlap(Ball,minimum):
            if not self.just_bounced:
                self.just_bounced = True
                self.score += abs(Ball.velocity.y)
            sign = +1 if self.position.x < Ball.position.x else -1
            if self.collision_area == self.PART.center:
                ball.position.x = self.position.x + minimum * sign
            else:
                ball.position.adjust(self.middle_point,minimum)
            ball.velocity.x = Ball(Ball.velocity.x, sign)
            ball.change_speed()
        else:
            self.just_bounced = False
                
            

class Ball:
    def __init__(self, x, y):
        """
        x -- starting x position \n
        y -- starting y position
        """
        self.obj = turtle.Turtle()
        self.obj.speed(2)
        self.obj.shape("square")
        self.obj.color("white")
        self.obj.penup()
        self.obj.goto(x,y)
        rad = math.pi*random.randint(10, 20)*16/180
        self.dx = 2*math.sqrt(2)*math.cos(rad)
        self.dy = 2*math.sqrt(2)*math.sin(rad)
    def reset(self, x, y):
        self.obj.goto(x,y)
        rad = math.pi*random.randint(5, 10)*32/180
        self.dx = 2*math.sqrt(2)*math.cos(rad)
        self.dy = 2*math.sqrt(2)*math.sin(rad)


paddle_a = Paddle(-350,0)
paddle_b = Paddle(350,0)
ball = Ball(0,0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 14, "normal"))

score_a = 0
score_b = 0

# Bind keys, also specifies which "paddle" the control is assigned to
wn.listen()
wn.onkeypress(paddle_a.up, "w")
wn.onkeypress(paddle_a.up, "W")
wn.onkeypress(paddle_a.down, "s")
wn.onkeypress(paddle_a.down, "S")
wn.onkeypress(paddle_b.up, "Up")
wn.onkeypress(paddle_b.down, "Down")

# main game loop

def mainloop():
    global score_a, score_b
    wn.update()
    # Update ball position
    ball.obj.setx(ball.obj.xcor()+ball.dx)
    ball.obj.sety(ball.obj.ycor()+ball.dy)

    # pos, validate, bounce
    if -360 < ball.obj.xcor() < -340 and paddle_a.obj.ycor() - 50 < ball.obj.ycor() < paddle_a.obj.ycor() + 50:
        ball.obj.setx(-340)
        ball.dx *= -1.05
        ball.dy *= 1.05
        #plays .wav on loop
        #mixer.music.play()

    if -360 < ball.obj.xcor() > 340 and paddle_b.obj.ycor() - 50 < ball.obj.ycor() < paddle_b.obj.ycor() + 50:
        ball.obj.setx(340)
        ball.dx *= -1.05
        ball.dy *= 1.05
        #mixer.music.play()

    if ball.obj.xcor() > 390:
        score_a += 1
        ball.reset(0, 0)
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font = ("Courier", 14, "normal"))

    if ball.obj.xcor() < -390:
        score_b += 1
        ball.reset(0, 0)
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font = ("Courier", 14, "normal"))


    if ball.obj.ycor() > 290:
        ball.obj.sety(290)
        ball.dy *= -1
        #mixer.music.play()

    if ball.obj.ycor() < -290:
        ball.obj.sety(-290)
        ball.dy *= -1
        #mixer.music.play()
    
    if score_a > 9 or score_b > 9:
        sys.exit()

    wn.ontimer(mainloop, 10)

try: 
    mainloop()
    turtle.mainloop()
except:
    pass