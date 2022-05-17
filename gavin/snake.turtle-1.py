
# We will need to use three standard modules
import turtle
import time
import random
import os
from math import sqrt 
from tkinter import PhotoImage, font
from playsound import playsound
# How fast our game loop should run
delay = 0.1
score = 0
high_score = 0

p = os.path.dirname(os.path.abspath(__file__))

# To create a window we use a function 
# from the turtle module called 'Screen()'
# We will put it in a variable called 'wn' (like window)

# This creates a new screen object in our wn variable
wn = turtle.Screen() 

# Set the title of the window by changing the "title" attribute
wn.title("Snake Game")

# The same goes for setting the background color of the window
wn.bgcolor("light blue")
wn.bgpic(f'{p}/assets/background (1).gif')

# Set the size of our window
wn.setup(width=600, height=600)

# Set the refresh rate
wn.tracer(0)

#pprint.pprint (vars(wn))
wn._root.resizable(False, False)

# images to load
snake_head_north = PhotoImage(file=f'{p}/assets/snake_head/snake_head-0.gif').zoom(3, 3).subsample(5, 5)
snake_head_east = PhotoImage(file=f'{p}/assets/snake_head/snake_head-1.gif').zoom(3, 3).subsample(5, 5)
snake_head_south = PhotoImage(file=f'{p}/assets/snake_head/snake_head-2.gif').zoom(3, 3).subsample(5, 5)
snake_head_west = PhotoImage(file=f'{p}/assets/snake_head/snake_head-3.gif').zoom(3, 3).subsample(5, 5)
food_1 = PhotoImage(file=f'{p}/assets/food.gif').zoom(3,3).subsample(5,5)
# loading images into window
wn.addshape("snake_head_north", turtle.Shape("image", snake_head_north))
wn.addshape("snake_head_east", turtle.Shape("image", snake_head_east))
wn.addshape("snake_head_south", turtle.Shape("image", snake_head_south))
wn.addshape("snake_head_west", turtle.Shape("image", snake_head_west))
wn.addshape("food_1",  turtle.Shape("image", food_1))

# Create a new turtle object, we'll call it 'head'
head = turtle.Turtle()

turtle.hideturtle()
# Set the shape of our turtle
head.shape("snake_head_north") #TODO: change

# Probably obvious what this does...
head.color("red")

# We dont want it to actually draw a line, just the turtle
head.penup()

# Move turtle to the middle of the screen (which is 0,0)
head.goto(0,0)

# We are setting a new value on this to keep track of
# what direction our snake is moving. At first we want it
# to be stopped
head.direction = "stop"
# Create our turtle food
food = turtle.Turtle()

# random.choice will return one random item from a list
colors = random.choice(['pink', 'purple', 'yellow','blue','red'])
shapes = random.choice(['square','triangle','circle'])

# This food isn't moving other than when it gets eaten
food.speed(0)

# Use the random shape we picked above
food = turtle.Turtle('food_1')

# Use the random color we picked above
food.color(colors)

food.penup()

# Start food at 100 pixels above the center
food.goto(0,100)
# Create scoreboard turtle
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,250)
pen.write(f"Snake Game", align="center",
    font=("Times New Roman",30,"bold"))
# We don't want to actually see the turtle
# We just want to use it's ability to print text
pen.hideturtle()

# This is where our text will start, 250 pixels above the center of the window
pen.goto(0,250)

# The .write() method writes text to the screen. You can see that it has several
#    parameters that allow changing the size, font, alignment, etc.
# This writes out our initial score, but we will use the same line
#    when we want to update our score later.
pen.hideturtle()


# If an 'up' key is hit
def goup():
    if head.direction != "down":
        head.direction = "up"
    head.shape("snake_head_north")
        
def godown():
    if head.direction != "up":
        head.direction = "down"
    head.shape("snake_head_south")
        
def goleft():
    if head.direction != "right":
        head.direction = "left"
    head.shape("snake_head_west")

def goright():
    if head.direction != "left":
        head.direction = "right"
    head.shape("snake_head_east")

def goup1():
    if head.direction != "down":
        head.direction = "up"
    head.shape("snake_head_north")
        
def godown1():
    if head.direction != "up":
        head.direction = "down"
    head.shape("snake_head_south")
        
def goleft1():
    if head.direction != "right":
        head.direction = "left"
    head.shape("snake_head_west")

def goright1():
    if head.direction != "left":
        head.direction = "right"
    head.shape("snake_head_east")

# Call this to move the head based on direction
def move():
    if head.direction == "up":
        # xcor() / ycor() can be used to GET the coordinates of the turtle
        y = head.ycor()
        # setx() / sety() can be used to SET the coordinates of the turtle
        # Add 20 to where we were, that moves us up the screen
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# Tell the window to start listening
wn.listen()

# When the window object sees a key get pressed (w in this case)
#    we tell it that it should call the 'goup' function.
wn.onkeypress(goup, "Up")

# Now we'll add the others
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
wn.onkeypress(goup1, "w")

# Now we'll add the others
wn.onkeypress(godown1, "s")
wn.onkeypress(goleft1, "a")
wn.onkeypress(goright1, "d")
segments = []
speed_counter = 0
# Main gameplay loop



# Hourglass shape
shape_vbody =((8, -12),(8, 12),
            (-8, -12),(-8, 12))
shape_hbody =((-12,8),(12,8),
            (-12,-8),(12,-8))
turtle.register_shape('v_hour_glass', shape_vbody)
turtle.register_shape('h_hour_glass', shape_hbody)

while True:
    # Tell our window to update
    wn.update()
        # Check for food consumption
    # Use the 'distance' method to see how far between two turtles
    if head.distance(food) < 20:
        # Move the food turtle to a new random location
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)
    
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('v_hour_glass')
        turtle.colormode(255)
        new_segment.color(76, 175, 79)
        new_segment.penup()
        
        # Add our segment to the list
        segments.append(new_segment)
        speed_counter = 40 # speed duration
        
        
        # Let's make our snake go a little faster by shortening delay some
    
        # Add 10 to our score
        score += 1
    
        # If our new score is > high_score, we have a new high score
        if score > high_score:
            high_score = score
        
        # Update score display
        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center",
            font=("Candara",30,"bold"))

    if speed_counter > 0:
        delay = 0.05 #Boost speed
        speed_counter -= 1
    else:
        delay = 0.1

    # Starting with newest segment, move each to position of previous segment
    for index in range(len(segments)-1, -1, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        if segments[index].xcor() == x:
            segments[index].shape('h_hour_glass')
        else:
            segments[index].shape('v_hour_glass')
            #TODO: moving along X axis (hor change)
        
        if segments[index] is segments[0]:
            if segments[index].xcor() == head.xcor():
                segments[index].shape('h_hour_glass')
            else:
                segments[index].shape('v_hour_glass')
        #TODO: index starts at bottom, if index is 0 (need to change for loop)
            #chekc against head.pos
            pass
        segments[index].goto(x,y)

    # If we have more than one segment, move the first segment to current head 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    # Move our head turtle if it has some direction set
    move()
        # Check to see if head is too close to any segment
    for segment in segments:
        if segment.distance(head) < 20:
            # Pause for a second so we can observer the disaster
            time.sleep(1)
            
            # Move head of snake back to center screen
            head.goto(0,0)
            
            # Don't move until we start again with a key press
            head.direction = "stop"

            # We don't want our segments hanging around onscreen
            #   so we'll move them so we can't see them. 
            #   Then we'll delete them.
            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

            # Reset current score
            score = 0

            # Reset delay
            delay = 0.1
            speed_counter = 0
            # Update score
            pen.clear()
            pen.write(f"Score : {score}  High Score : {high_score}", align="center",
                font=("candara",30,"bold"))
                
    # Check for too close to a wall
    
    # We'll count anything within 10px of any edge as a hit
    # Since our window is assumed to be 600x600 and center is 0,0
    #   our boundaries are:
    #   Left side = -(600/2)+10
    #   Right side = (600/2)-10
    #   Etc. - For now, these numbers are fine.
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        speed_counter = 0
        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center",
            font=("candara",30,"bold"))
    time.sleep(delay)

    turtle.hideturtle