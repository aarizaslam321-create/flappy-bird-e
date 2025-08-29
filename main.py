# Imports
import turtle, time, random

# Turtle Shape
turtle.register_shape("bird.gif")

# Setting up the screen
window = turtle.Screen()
window.title("Flappy Bird")
window.bgpic("background.gif")
window.bgcolor("light blue")
window.setup(width=500, height=600)
window.tracer(0)

# Window Lock
root = window.getcanvas().winfo_toplevel()
root.resizable(False, False)

# Setting up the player turtle
player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("bird.gif")
player.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
player.goto(-200, 0)
player.dx = 0
player.dy = 1

# Setting up the pen turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write("0", move= False, align= "center", font= ("Arial", 30, "bold"))

# Setting up top pipe 1
pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("light green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=40, stretch_len=3, outline=None)
pipe1_top.goto(300, 475)
pipe1_top.dx = -2
pipe1_top.dy = 0
pipe1_top.value = 1

# Setting up bottom pipe 1
pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("light green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=40, stretch_len=3, outline=None)
pipe1_bottom.goto(300, -475)
pipe1_bottom.dx = -2
pipe1_bottom.dy = 0

# Setting up top pipe 2
pipe2_top = turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("light green")
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=40, stretch_len=3, outline=None)
pipe2_top.goto(600, 575)
pipe2_top.dx = -2
pipe2_top.dy = 0
pipe2_top.value = 1

# Setting up bottom pipe 2
pipe2_bottom = turtle.Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("light green")
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(stretch_wid=40, stretch_len=3, outline=None)
pipe2_bottom.goto(600, -375)
pipe2_bottom.dx = -2
pipe2_bottom.dy = 0

# Game Variables
gravity = -0.3
player.score = 0
print(f"SCORE: {player.score}")
isPlaying = False

# Define Functions
def go_up():
    player.dy = player.dy + 8
    if player.dy > 8:
        player.dy = 8

def go_down():
    player.dy = player.dy - 3
    if player.dy > -6:
        player.dy = -6

def super_jump():
    player.dy = player.dy + 14
    if player.dy > 50:
        player.dy = 50

def restart():
    # Reset Score
    player.score = 0

    # Move the pipes back
    pipe1_top.setx(300)
    pipe1_bottom.setx(300)
    pipe2_top.setx(600)
    pipe2_bottom.setx(600)

    # Speed of pipes reset
    pipe1_top.dx = -2
    pipe1_bottom.dx = -2
    pipe2_top.dx = -2
    pipe2_bottom.dx = -2

    # Moving the player back
    player.goto(-200, 0)
    player.dy = 0

    # Moving text back
    pen.clear()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.color("white")
    pen.goto(0,250)
    pen.write("0", move= False, align= "center", font= ("Arial", 32, "bold"))

def kill():
    # Game Over  
    pen.clear()
    pen.color("red")
    pen.goto(0,0)
    pen.write("You died!", move= False, align= "center", font= ("Arial", 50, "bold"))
    window.update()
    time.sleep(3)
    restart()

# Keyboard
window.listen()
window.onkeypress(go_up, "space")
window.onkeypress(go_up, "Up")
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "Down")
window.onkeypress(restart, "r")
window.onkeypress(super_jump, "y")

# Main Game Loop
while True:
    # pause
    time.sleep(0.02)
    # screen update
    window.update()

    # add gravity
    player.dy = player.dy + gravity

    # Speed Up Pipes
    pipe1_top.dx -= 0.002
    pipe1_bottom.dx -= 0.002
    pipe2_top.dx -= 0.002
    pipe2_bottom.dx -= 0.002

    # Moving the player
    y = player.ycor()
    y = y + player.dy
    player.sety(y)

    # Bottom Border
    if player.ycor() < -290:
        player.sety(-290)
        player.dy = 0
        print("KILL")
        kill()

    # Top Border
    if player.ycor() > 290:
        player.sety(290)
        player.dy = 0

    # Moving pipes 1
    x = pipe1_top.xcor() 
    x = x + pipe1_top.dx
    pipe1_top.setx(x)

    x = pipe1_bottom.xcor() 
    x = x + pipe1_bottom.dx
    pipe1_bottom.setx(x)

    # return pipes 1 to start
    if pipe1_top.xcor() < -280:
        y = random.randint(175,675)
        pipe1_top.goto(350, y)
        pipe1_bottom.goto(350, y - 975)
        pipe1_top.value = 1

    # Moving pipes 2
    x = pipe2_top.xcor() 
    x = x + pipe2_top.dx
    pipe2_top.setx(x)

    x = pipe2_bottom.xcor() 
    x = x + pipe2_bottom.dx
    pipe2_bottom.setx(x)

    # return pipes 2 to start
    if pipe2_top.xcor() < -280:
        y = random.randint(175,675)
        pipe2_top.goto(350, y)
        pipe2_bottom.goto(350, y - 975)
        pipe2_top.value = 1

    # check for collision with pipe 1
    if (player.xcor() + 10 > pipe1_top.xcor() - 30) and (player.xcor() - 10 < pipe1_top.xcor() + 30):
        if (player.ycor() + 10 > pipe1_top.ycor() - 390) or (player.ycor () - 10 < pipe1_bottom.ycor() + 390):
             print("COLLISION")
             kill()

    # the score checker for pipe 1
    if pipe1_top.xcor() + 30 < player.xcor() - 10:
        player.score = player.score + pipe1_top.value
        pipe1_top.value = 0
        print(f"SCORE: {player.score}")
        pen.clear()
        pen.write(player.score, move= False, align= "center", font= ("Arial", 32, "bold"))

    # check for collision with pipe 2
    if (player.xcor() + 10 > pipe2_top.xcor() - 30) and (player.xcor() - 10 < pipe2_top.xcor() + 30):
        if (player.ycor() + 10 > pipe2_top.ycor() - 390) or (player.ycor () - 10 < pipe2_bottom.ycor() + 390):
            print("COLLISION") 
            kill()

    # the score checker for pipe 2
    if pipe2_top.xcor() + 30 < player.xcor() - 10:
        player.score = player.score + pipe2_top.value
        pipe2_top.value = 0
        print(f"SCORE: {player.score}")
        pen.clear()
        pen.write(player.score, move= False, align= "center", font= ("Arial", 32, "bold"))