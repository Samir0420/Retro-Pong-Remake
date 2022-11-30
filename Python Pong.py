#Simple Pong Game in Python 3

#Import the turtle module
import turtle

#Window
window_screen = turtle.Screen() #Create the window using the turtle module
window_screen.title("Pong Reloded by Samir") #Name the window "Pong Reloded by Samir"
window_screen.bgcolor ("white") #The background color is set to white
window_screen.setup (width = 800, height = 600) #Dimensions for window
window_screen.tracer (0)

#Score
score_left = 0
score_right = 0

#Paddle Left
leftPaddle = turtle.Turtle() #Create the left paddle
leftPaddle.speed (0) 
leftPaddle.shape ("square") #Shape of paddle is square
leftPaddle.shapesize (stretch_wid = 4,stretch_len = 1) #Stretch to make the paddle a rectangle
leftPaddle.color ("red") #Set color to red
leftPaddle.penup()
leftPaddle.goto(-350,0) #Start location

#Paddle Right
rightPaddle = turtle.Turtle() #Create right paddle
rightPaddle.speed (0)
rightPaddle.shape ("square") #Shape of paddle is square
rightPaddle.shapesize (stretch_wid = 4,stretch_len = 1) #Stretch to make the paddle a rectangle
rightPaddle.color ("blue") #Set color to blue
rightPaddle.penup()
rightPaddle.goto(350,0)#Start location

#PongBall
pongBall = turtle.Turtle() #Create the pong ball using the turtle module
pongBall.speed (0)
pongBall.shape ("circle") #The shape of the ball will be a circle
pongBall.color ("aqua") #Set the color of the ball aqua
pongBall.penup()
pongBall.goto(0,0) #Set the start location to be at (0,0)

pongBall.dx = 0.3
pongBall.dy = -0.3

#Pen
pen = turtle.Turtle()
pen.speed (0)
pen.color ("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Left: 0   Player Right: 0", align="center", font=("Impact", 24, "normal"))

#Paddle Movement

#Left Paddle

#Function to move left paddle up
def leftPaddle_up ():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

#Function to move left paddle down
def leftPaddle_down ():
    y = leftPaddle.ycor()
    y -= 20
    leftPaddle.sety(y)

#Right Paddle

#Function to move right paddle up
def rightPaddle_up ():
    y = rightPaddle.ycor()
    y += 20
    rightPaddle.sety(y)

#Function to move right paddle down
def rightPaddle_down ():
    y = rightPaddle.ycor()
    y -= 20
    rightPaddle.sety(y)

#Keyboard Binding (Left)
window_screen.listen()
window_screen.onkeypress(leftPaddle_up, "w")
window_screen.onkeypress(leftPaddle_down, "s")

#Keyboard Binding (Right)
window_screen.listen()
window_screen.onkeypress(rightPaddle_up, "Up")
window_screen.onkeypress(rightPaddle_down, "Down")

#Main Game Loop
while True:
    window_screen.update()

    #Move the pongBall
    pongBall.setx(pongBall.xcor() + pongBall.dx)
    pongBall.sety(pongBall.ycor() + pongBall.dy)

    #Boarder Checking
    if pongBall.ycor () > 290:
        pongBall.sety(290)
        pongBall.dy *= -1

    if pongBall.ycor () < -290:
        pongBall.sety(-290)
        pongBall.dy *= -1

    if pongBall.xcor () > 390:
        pongBall.goto(0, 0)
        pongBall.dx *= -1
        score_left += 1
        pen.clear()
        pen.write("Player Left: {}   Player Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))

    if pongBall.xcor () < -390:
        pongBall.goto(0, 0)
        pongBall.dx *= -1
        score_right += 1
        pen.clear()
        pen.write("Player Left: {}   Player Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))


    #Paddle and pongBall Collisions
    if (pongBall.xcor() > 340 and pongBall.xcor() < 350) and (pongBall.ycor() < rightPaddle.ycor() + 50 and pongBall.ycor() > rightPaddle.ycor() -50):
        pongBall.setx(340)
        pongBall.dx *= -1

    if (pongBall.xcor() < -340 and pongBall.xcor() > -350) and (pongBall.ycor() < leftPaddle.ycor() + 50 and pongBall.ycor() > leftPaddle.ycor() -50):
        pongBall.setx(-340)
        pongBall.dx *= -1
   
