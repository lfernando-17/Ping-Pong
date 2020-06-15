import os
import turtle

window = turtle.Screen()
window.setup(1280,720)
window.title("Ping Pong")
window.bgpic("background.gif")
#window.bgcolor("Black")
window.tracer(0)


#player1

player1 = turtle.Turtle()
player1.penup()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.goto(-500,0)
player1.shapesize(8,1)



player2 = turtle.Turtle()
player2.penup()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.goto(500,0)
player2.shapesize(8,1)



#bola
ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.goto(0,0)
ball.shapesize(1,1)
ball.velx = 1
ball.vely = 1

#score
score=turtle.Turtle()
score.penup()
score.speed(0)
score.shape("square")
score.color("white")
score.hideturtle()
score.goto(0,320)
score.a = 0
score.b = 0
score.write(f'Score A : {score.a}   Score I.A : {score.b}',align="center",font=("Bold",20))
def up():
    y = player1.ycor()
    y += 40
    player1.sety(y)
    if player1.ycor() >= 280 :
        player1.sety(280)
    elif player1.ycor()<= -280:
        player1.sety(-280)
def down():
    y = player1.ycor()
    y -= 40
    player1.sety(y)
    if player1.ycor() >= 280:
        player1.sety(280)
    elif player1.ycor() <= -280:
        player1.sety(-280)
def placar():
    ball.goto(0,0)
    score.clear()
    ball.velx *= -1
    score.write(f'Score A : {score.a}   Score I.A : {score.b}', align="center", font=("Bold", 20))


def move_ball():
    ball.setx(ball.xcor() + ball.velx)
    ball.sety(ball.ycor() + ball.vely)
    player2.sety(ball.ycor())
    if player2.ycor() >= 280:
        player2.sety(280)
    elif player2.ycor() <= -280:
        player2.sety(-280)
    if ball.xcor() > 600:
        score.a += 1
        placar()
    elif ball.xcor() < -600:
        score.b += 1
        placar()

    if ball.ycor() > 350:
        ball.vely *= -1
    elif ball.ycor() < -350:
        ball.vely *= -1
def colision():
    if ball.xcor() < -480 and ball.ycor() <player1.ycor() + 90  and ball.ycor() > player1.ycor()-90:
        ball.setx(-480)
        ball.velx *= -1

    elif ball.xcor() > 480 and ball.ycor() <player2.ycor() + 90  and ball.ycor() > player2.ycor()-90:
        ball.setx(480)
        ball.velx *= -1
window.listen()
window.onkeypress(up, "w")
window.onkeypress(down, "s")
while True:
    move_ball()
    colision()
    window.update()



#Assim , ou eu faco um while True : window.update()
#window.mainloop()