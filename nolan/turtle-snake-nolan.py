
# We will need to use three standard modules
import turtle
import time
import random
#from playsound import playsound
from tkinter import PhotoImage
import os
import requests
import pygame

p = os.path.dirname(os.path.abspath(__file__))

game_title = 'Mommy (Nolan)'
hs_link = 'http://api.snakegame.cf/scores'
player_name = "???"

# Load audio
pygame.mixer.init()
snd_mommy = pygame.mixer.Sound(f"{p}/sounds/oh-mommy.wav")
snd_send_mommy = pygame.mixer.Sound(f"{p}/sounds/send-mommy.wav")

# How fast our game loop should run
delay = 0.1
score = 0
high_score = 0
# To create a window we use a function 
# from the turtle module called 'Screen()'
# We will put it in a variable called 'wn' (like window)

# This creates a new screen object in our wn variable
wn = turtle.Screen() 

# Set the title of the window by changing the "title" attribute
wn.title("Snake Game")

# The same goes for setting the background color of the window
wn.bgcolor("blue")

# Set the size of our window
wn.setup(width=800, height=800)

# Set the refresh rate
wn.tracer(0)
# Create a new turtle object, we'll call it 'head'
image_sample = PhotoImage(file = f"{p}/pyphotos/face.gif",)
image_sample1 = PhotoImage(file = f"{p}/pyphotos/car.gif",)
image_sample = image_sample.subsample(8)
image_sample1 = image_sample1.subsample(8)
wn.addshape("face.gif", turtle.Shape("image", image_sample))
wn.addshape("car.gif", turtle.Shape("image",image_sample1))
head = turtle.Turtle("face.gif")

# Set the shape of our turtle
# head.shape("triangle")

# Probably obvious what this does...
head.color("orange")

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
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square','triangle','circle'])

# This food isn't moving other than when it gets eaten
food.speed(0)

# Use the random shape we picked above
food.shape(shapes)

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

# We don't want to actually see the turtle
# We just want to use it's ability to print text
pen.hideturtle()

# This is where our text will start, 250 pixels above the center of the window
pen.goto(0,250)

# The .write() method writes text to the screen. You can see that it has several
#    parameters that allow changing the size, font, alignment, etc.
# This writes out our initial score, but we will use the same line
#    when we want to update our score later.
pen.write(f"Score : {score}  High Score : {high_score}", align="center",
    font=("candara",24,"bold"))
# If an 'up' key is hit
def goup():
    if head.direction != "down":
        head.direction = "up"
        
def godown():
    if head.direction != "up":
        head.direction = "down"
        
def goleft():
    if head.direction != "right":
        head.direction = "left"
        
def goright():
    if head.direction != "left":
        head.direction = "right"
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
wn.onkeypress(goup, "w")
wn.onkeypress(goup, "Up")

# Now we'll add the others
wn.onkeypress(godown, "s")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "a")
wn.onkeypress(goleft,"Left")
wn.onkeypress(goright, "d")
wn.onkeypress(goright, "Right")

# Create an empty list
segments = []
# Main gameplay loop
while True:
    # Tell our window to update
    wn.update()
      # Check for food consumption
    # Use the 'distance' method to see how far between two turtles
    if head.distance(food) < 20:
        # Move the food turtle to a new random location
        x = random.randint(-500,500)
        y = random.randint(-500,500)
        food.goto(x,y)
        
    
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("car.gif")
        new_segment.color("orange")
        new_segment.penup()
        
        
        # Add our segment to the list
        segments.append(new_segment)

       # playsound(f'{p}/sounds/oh-mommy.wav',False)
        pygame.mixer.Sound.play(snd_mommy)
    
        # Let's make our snake go a little faster by shortening delay some
        delay -= 0.001
    
        # Add 10 to our score
        score += 10
    
        # If our new score is > high_score, we have a new high score
        if score > high_score:
            high_score = score
        
         # Update score display
        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center",
            font=("candara",24,"bold"))
    # Starting with newest segment, move each to position of previous segment
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
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
            #playsound(f'{p}/sounds/send-mommy.wav')
            pygame.mixer.Sound.play(snd_send_mommy)
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

            # Save score to leaderboard
            try:
                data=f'"name": "{player_name}", "score": "{score}", "game": "{game_title}"'
                data = '{' + data + '}'
                r = requests.post(f'{hs_link}', headers={'Content-Type': 'application/json'}, data=data)
            except:
                print(f'Failed to post high score: {r.status_code}')

            # Reset current score
            score = 0
            
            # Reset delay
            delay = 1
            
            # Update score
            pen.clear()
            pen.write(f"Score : {score}  High Score : {high_score}", align="center",
                font=("candara",24,"bold"))
    # Check for too close to a wall
    
    # We'll count anything within 10px of any edge as a hit
    # Since our window is assumed to be 600x600 and center is 0,0
    #   our boundaries are:
    #   Left side = -(600/2)+10
    #   Right side = (600/2)-10
    #   Etc. - For now, these numbers are fine.
    w = wn.window_width()
    h = wn.window_height()
    if head.xcor() > w/2 or head.xcor() < w/-2 or head.ycor() > h/2 or head.ycor()  < h/-2:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        #playsound(f'{p}/sounds/send-mommy.wav')
        pygame.mixer.Sound.play(snd_send_mommy)

        # Save score to leaderboard
        try:
            data=f'"name": "{player_name}", "score": "{score}", "game": "{game_title}"'
            data = '{' + data + '}'
            r = requests.post(f'{hs_link}', headers={'Content-Type': 'application/json'}, data=data)
        except:
            print(f'Failed to post high score: {r.status_code}')

        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center",
            font=("candara",24,"bold"))
    time.sleep(delay)
