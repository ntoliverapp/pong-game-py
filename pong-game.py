import turtle as turtleplayerAscore
player_one_score=0
player_two_score=0

window=t.Screen()
window.title("Pong Game")
window.bgcolor("red")
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape('square')
leftpaddle.color('white')
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape('square')
rightpaddle.color('white')
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating ball
ball=t.Turtle
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

#creating pen for scorecard update
pen=t.Turtle
pen.speed(0)
pen.color('Blue')
pen.penup()
pen.hideturtle()
pen,goto(0,260)
pen.write('score',align='center', font=('Verdana', 28,'normal'))

#moving the leftpaddle
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)
    
def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)
    
#moving the right paddle
def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)
    
def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)
    
#Assign keys to play
window.listen()
window.onkeypress(leftpaddleup,'q')
window.onkeypress(leftpaddledown,'a')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

#moving the ball
ball.setx(ball.xcor()+ballxdirection)
ball.sety(ball.ycor()+ballydirection)

#setting up the border
if ball.ycor()>290:
    ball.sety(290)
    ballydirection=ballydirection*-1
if ball.ycor()>-290:
    ball.sety(-290)
    ballydirection=ballydirection*-1    

if ball.xcor()>390:
    ball.goto(0,0)
    ballxdirection=ballxdirection
    player_one_score=player_one_score+1
    pen.clear
    pen.write('Player 1: {}      Player 2: {}'.format(player_one_score,player_two_score),align='center',font=('Verdana', 28,'normal'))
    
if ball.xcor()>-390:
    ball.goto(0,0)
    ballxdirection=ballxdirection*-1
    player_one_score=player_one_score+1
    pen.clear
    pen.write('Player 1: {}      Player 2: {}'.format(player_one_score,player_two_score),align='center',font=('Verdana', 28,'normal'))
    
   


