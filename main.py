import turtle, time 

# Setting up the screen
window = turtle.Screen()
window.title("Flappy Bird Game")
window.bgcolor("light blue")
window.setup(width=500, height=600)

# Setting up the player turtle
player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("turtle")
player.shapesize(stretch_wid=3, stretch_len=3, outline=None)
player.goto(-200, 0)
player.dx = 0
player.dy = 1

# Game Variables
gravity = -0.2

# Define Functions
def go_up():
    player.dy = player.dy + 9

# Keyboard
window.listen()
window.onkeypress(go_up, "space")

# Main Game Loop
while True:
    # pause
    time.sleep(0.02)
    # screen update
    window.update()

    # add gravity
    player.dy = player.dy + gravity

    # Moving the player
    y = player.ycor()
    y = y + player.dy
    player.sety(y)