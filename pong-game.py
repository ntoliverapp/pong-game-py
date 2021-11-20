import turtle as t


player_one_score=0
player_two_score=0

window=t.Screen()
window.title('Ping-Pong Game')
window.bgcolor('#162521')
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
left_paddle=t.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('#c0e0de')
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350,0)


#creating right paddle
right_paddle=t.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('#c0e0de')
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(350,0)

#creating ball
ball=t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball_x_direction=1.5
ball_y_direction=1.5

#creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score',align='center', font=('comic sans MS', 20,'normal'))



#moving the leftpaddle
def left_paddle_up():
    y = left_paddle.ycor()
    y = y + 15
    left_paddle.sety(y)
    
def left_paddle_down():
    y = left_paddle.ycor()
    y = y - 15
    left_paddle.sety(y)
    
#moving the right paddle
def right_paddle_up():
    y = right_paddle.ycor()
    y = y + 15
    right_paddle.sety(y)
    
def right_paddle_down():
    y = right_paddle.ycor()
    y = y - 15
    right_paddle.sety(y)
    
#Assign keys to play
window.listen()
window.onkeypress(left_paddle_up,'a')
window.onkeypress(left_paddle_down,'z')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')

while True:
    window.update()
    

#moving the ball
    ball.setx(ball.xcor() + ball_x_direction)
    ball.sety(ball.ycor() + ball_y_direction)

#setting up the border
    if ball.ycor() > 290: #right top paddle border
        ball.sety(290)
        ball_y_direction = ball_y_direction * -1
    
    if ball.ycor()< -290: #left top paddle border
        ball.sety(-290)
        ball_y_direction = ball_y_direction * -1    
        

    if ball.xcor() > 390: #right width paddle border
        ball.goto(0,0)
        ball_x_direction = ball_x_direction * -1
        player_one_score = player_one_score + 1
        pen.clear()
        pen.write('Player 1: {}                Player 2: {}'.format(player_one_score,player_two_score),align='center',font=('comic sans MS', 20,'normal'))
  
    
    if ball.xcor() < -390: #left width paddle border
        ball.goto(0,0)
        ball_x_direction = ball_x_direction * -1
        player_two_score = player_two_score + 1
        pen.clear()
        pen.write('Player 1: {}                Player 2: {}'.format(player_one_score,player_two_score),align='center',font=('comic sans MS', 20,'normal'))

    
#Handling the Collisions
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() -40):
        ball.setx(340)
        ball_x_direction = ball_x_direction * -1

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() +40 and ball.ycor() > left_paddle.ycor() -40):
        ball.setx(-340)
        ball_x_direction = ball_x_direction * -1
 



 

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   


