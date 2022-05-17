from cProfile import label
from math import pi
import tkinter
import pygame
import os
from playsound import playsound
import turtle
import time
import random
import pprint
from tkinter import BOTTOM, W, LEFT, Label, Entry, BOTH, VERTICAL, PhotoImage, PanedWindow, Tk # resize

p = os.path.dirname(os.path.abspath(__file__))

pygame.mixer.init()
s_boom = pygame.mixer.Sound(f'{p}/sounds/boom.wav')
s_rip = pygame.mixer.Sound(f'{p}/sounds/rip.wav')
s_screamed = pygame.mixer.Sound(f'{p}/sounds/screamed.wav')
s_scary = pygame.mixer.Sound(f'{p}/sounds/scary.wav')
s_oof = pygame.mixer.Sound(f'{p}/sounds/oof.wav')


# How fast our game loop should run
delay = 0.1

score = 0 
high_score = 0 
high_scores = []
keychange = 0
keyset = "normal"
# To create a window we use a function 
# from the turtle module called 'Screen()'
# We will put it in a variable called 'wn' (like window)

# This creates a new screen object in our wn variable
wn = turtle.Screen()

# Set the title of the window by changing the "title" attribute
wn.title("this game was a mistake")

# no resize for both directions

# start a program
# The same goes for setting the background color of the window
wn.bgpic(f"{p}/images/me2.gif")
wn.bgcolor("gray")

# Set the size of our window
wn.setup(width=1400, height=600)

# Set the refresh rate
wn.tracer(0)

#pprint.pprint (vars(wn))
wn._root.resizable(False, False)

# Create a new turtle object, we'll call it 'head'
image_sample = PhotoImage(file=f"{p}/images/me.gif").subsample(2, 2)
image_sample2 = PhotoImage(file=f"{p}/images/xd.gif").subsample(1, 1)
image_sample3 = PhotoImage(file=f"{p}/images/xd2.gif").subsample(1, 1)
image_sample4 = PhotoImage(file=f"{p}/images/xd3.gif").subsample(1, 1)
image_sample5 = PhotoImage(file=f"{p}/images/xd4.gif").subsample(1, 1)
image_sample6 = PhotoImage(file=f"{p}/images/xd5.gif").subsample(1, 1)
image_sample7 = PhotoImage(file=f"{p}/images/xd6.gif").subsample(1, 1)
image_sample8 = PhotoImage(file=f"{p}/images/xd7.gif").subsample(1, 1)
image_sample9 = PhotoImage(file=f"{p}/images/xd8.gif").subsample(1, 1)
image_sample10 = PhotoImage(file=f"{p}/images/xd9.gif").subsample(1, 1)
image_sample11 = PhotoImage(file=f"{p}/images/xd10.gif").subsample(1, 1)
image_sample12 = PhotoImage(file=f"{p}/images/xd11.gif").subsample(2, 2)
image_sample13 = PhotoImage(file=f"{p}/images/xd12.gif").subsample(2, 2)
image_sample14 = PhotoImage(file=f"{p}/images/xd13.gif").subsample(2, 2)
image_sample15 = PhotoImage(file=f"{p}/images/xd14.gif").subsample(2, 2)
# add the image to window
wn.addshape("image_sample", turtle.Shape("image", image_sample)) # 1st 'loads' picture
wn.addshape("image_sample2", turtle.Shape("image", image_sample2))
wn.addshape("image_sample3", turtle.Shape("image", image_sample3))
wn.addshape("image_sample4", turtle.Shape("image", image_sample4))
wn.addshape("image_sample5", turtle.Shape("image", image_sample5))
wn.addshape("image_sample6", turtle.Shape("image", image_sample6))
wn.addshape("image_sample7", turtle.Shape("image", image_sample7))
wn.addshape("image_sample8", turtle.Shape("image", image_sample8))
wn.addshape("image_sample9", turtle.Shape("image", image_sample9))
wn.addshape("image_sample10", turtle.Shape("image", image_sample10))
wn.addshape("image_sample11", turtle.Shape("image", image_sample11))
wn.addshape("image_sample12", turtle.Shape("image", image_sample12))
wn.addshape("image_sample13", turtle.Shape("image", image_sample13))
wn.addshape("image_sample14", turtle.Shape("image", image_sample14))
wn.addshape("image_sample15", turtle.Shape("image", image_sample15))
is_muted = False

# put image in the parenthesis that you want the snake head to be
head = turtle.Turtle('image_sample')

# Set the shape of our turtle
# head.shape("images/me.gif")

# Probably obvious what this does...
head.color("white")

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
colors = random.choice(['white', 'black'])
shapes = random.choice(['square','triangle','circle'])

# This food isn't moving other than when it gets eaten
food.speed(0)

# Use the random shape we picked above
food = turtle.Turtle('image_sample')

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

pen.goto(0,-230)

pen.write(f"Warning: Loud Sounds Eminent. You have been warned.", align="center",
    font=("Comic Sans MS",15,"bold","italic"))

pen.goto(0,250)

pen.write(f"The worst snake game you'll ever play :)", align="center",
    font=("Times New Roman",25,"bold", "italic"))


# We don't want to actually see the turtle
# We just want to use it's ability to print text
pen.hideturtle()

# This is where our text will start, 250 pixels above the center of the window
pen.goto(0,230)

l_font = ("Arial", 10)
s_font = ("Arial", 8)

p1 = PanedWindow(orient=VERTICAL)
p1.place(width=400, height=600, x=0)
#left = Label(p1, text="Left Panel")
#p1.add(left)
p1.add(Label(p1, text="Leaderboard"))
p1.add(Label(p1, text="____________________________________________________________________"))
lb_labels = []
for c in range(0,10):
    l = Label(p1, text=f"{c+1}. --- | --")
    lb_labels.append(l)
    p1.add(l)
p1.add(Label(p1, text="_____________________________________________________________________"))
p1.add(Label(p1, text="Note"))
p1.add(Label(p1, text="------------------------------------"))
p1.add(Label(p1, text="When entering your name, Press the tab button to exit out of the window", font=s_font))
p1.add(Label(p1, text="_____________________________________________________________________"))
p1.add(Label(p1, text="Enter Name in the white box below:"))
p1.add(Label(p1, text="_____________________________________________________________________"))
p1.add(Label(p1, text=" "))
high_score_name = Entry(p1,width=4)
high_score_name.place(x=10,y=470,width=200,height=25)


p2 = PanedWindow(orient=VERTICAL)
p2.place(width=400, height=600, x=1000)

#left = Label(p1, text="Left Panel")
#p1.add(left)

p2.add(Label(p2, text="Controls/Manual/info"))
p2.add(Label(p2, text="____________________________________________________________________"))
p2.add(Label(p2, text="/ | Cycles Through a Variety of Preset Keysets (Recommended for QOL)", font=s_font))
p2.add(Label(p2, text="--------------------------------------------------------------------"))
p2.add(Label(p2, text="1. WASD"))
p2.add(Label(p2, text="2. All Arrow Keys"))
p2.add(Label(p2, text="3. TFGH"))
p2.add(Label(p2, text="4. WASD but Backwards"))
p2.add(Label(p2, text="5. COUK"))
p2.add(Label(p2, text="6. 3490"))
p2.add(Label(p2, text="____________________________________________________________________"))
p2.add(Label(p2, text="- | Increases the Speed every time it is pressed"))
p2.add(Label(p2, text="= | Decreases the Speed every time it is pressed"))
p2.add(Label(p2, text="____________________________________________________________________"))
p2.add(Label(p2, text="[ | Increases the Score every time it is pressed"))
p2.add(Label(p2, text="] | Decreases the Score every time it is pressed"))
p2.add(Label(p2, text="____________________________________________________________________"))
p2.add(Label(p2, text=", | Mutes All Audio (Recommended)"))
p2.add(Label(p2, text=". | Unmutes All Audio"))
p2.add(Label(p2, text="____________________________________________________________________"))
p2.add(Label(p2, text="Credits / Playtesters"))
p2.add(Label(p2, text="____________________________________________________________________"))
p2.add(Label(p2, text="Playtesters: Jesus Boy ", font=s_font))
p2.add(Label(p2, text="Main Code/Helped: Jayden, C. Brown, Anonymous Friend ", font=s_font))
p2.add(Label(p2, text="Edited Code/Project Manager/Voice Actor For the Death SFX: Collin R ", font=s_font))


# The .write() method writes text to the screen. You can see that it has several
#    parameters that allow changing the size, font, alignment, etc.
# This writes out our initial score, but we will use the same line
#    when we want to update our score later.


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

def increase():
    global delay
    delay -= 0.003

def decrease():
    global delay
    delay += 0.003

def scoreinc():
    global score
    score += 1

def scoredec():
    global score
    score -= 1

def mute():
    global is_muted
    is_muted = True

def unmute():
    global is_muted
    is_muted = False

def set_high_scores():
    n = high_score_name.get()
    if len(high_scores) == 0:
        high_scores.append({'name':n, 'score':score})
    else :
        score_set = False
        for c in range(0, len(high_scores)):
            if score >= high_scores[c]['score'] and score_set == False:
                high_scores.insert(c, {'name':n, 'score':score}) 
                score_set = True

        if score_set == False:
            high_scores.append({'name':n, 'score':score})
    for c in range(0,min(10,len(high_scores))):
        lb_labels[c].configure(text=f"{c+1}. {high_scores[c]['name']} | {high_scores[c]['score']}")

    print(high_scores)
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

def change_keyset(change_to):
    global keyset
    wn.onkeypress(None, "w")
    wn.onkeypress(None, "a")
    wn.onkeypress(None, "s")
    wn.onkeypress(None, "d")
    wn.onkeypress(None, "Right")
    wn.onkeypress(None, "Left")
    wn.onkeypress(None, "Up")
    wn.onkeypress(None, "Down")
    wn.onkeypress(None, "t")
    wn.onkeypress(None, "g")
    wn.onkeypress(None, "f")
    wn.onkeypress(None, "h")
    wn.onkeypress(None, "c")
    wn.onkeypress(None, "o")
    wn.onkeypress(None, "u")
    wn.onkeypress(None, "k")
    wn.onkeypress(None, "3")
    wn.onkeypress(None, "4")
    wn.onkeypress(None, "9")
    wn.onkeypress(None, "0")
    if change_to == "normal":
        wn.onkeypress(goup, "w")
        wn.onkeypress(godown, "s")
        wn.onkeypress(goleft, "a")
        wn.onkeypress(goright, "d")
        keyset = "normal"
        print(keyset)
    elif change_to == "arrows":
        wn.onkeypress(goup, "Up")
        wn.onkeypress(godown, "Down")
        wn.onkeypress(goleft, "Left")
        wn.onkeypress(goright, "Right")
        keyset = "arrows"
        print(keyset)
    elif change_to == "set":
        wn.onkeypress(goup, "t")
        wn.onkeypress(godown, "g")
        wn.onkeypress(goleft, "f")
        wn.onkeypress(goright, "h")
        keyset = "set"
        print(keyset)
    elif change_to == "backwards":
        wn.onkeypress(goup, "s")
        wn.onkeypress(godown, "w")
        wn.onkeypress(goleft, "d")
        wn.onkeypress(goright, "a")
        keyset = "backwards"
        print(keyset)
    elif change_to == "horrible":
        wn.onkeypress(goup, "c")
        wn.onkeypress(godown, "o")
        wn.onkeypress(goleft, "u")
        wn.onkeypress(goright, "k")
        keyset = "horrible"
        print(keyset)
    elif change_to == "mania":
        wn.onkeypress(goup, "3")
        wn.onkeypress(godown, "4")
        wn.onkeypress(goleft, "9")
        wn.onkeypress(goright, "0")
        keyset = "mania"
        print(keyset)

# Tell the window to start listening
def toggle_keyset():
    if keyset == "normal":
        change_keyset("arrows")
    elif keyset == "arrows":
        change_keyset("set")
    elif keyset == "set":
        change_keyset("backwards")
    elif keyset == "backwards":
        change_keyset("horrible")
    elif keyset == "horrible":
        change_keyset("mania")
    elif keyset == "mania":
        change_keyset("normal")

def image_change():
    img = "image_sample2"
    if high_score > 20000:
        img = "image_sample13"
    elif high_score > 15000:
        img = "image_sample12"
    elif high_score > 10000:
        img = "image_sample14"
    elif high_score > 5000:
        img = "image_sample15"
    elif high_score > 2500:
        img = "image_sample11"
    elif high_score > 1000:
        img = "image_sample10"
    elif high_score > 500:
        img = "image_sample9"
    elif high_score > 200:
        img = "image_sample8"
    elif high_score > 150:
        img = "image_sample7"
    elif high_score > 100:
        img = "image_sample6"
    elif high_score > 75:
        img = "image_sample5"
    elif high_score > 50:
        img = "image_sample4"
    elif high_score > 25:
        img = "image_sample3"

    for s in segments:
        s.shape(img)

    
wn.listen()

change_keyset("normal")
# When the window object sees a key get pressed (w in this case)
#    we tell it that it should call the 'goup' function.


wn.onkeypress(increase, "-")
wn.onkeypress(decrease, 'equal')

wn.onkeypress(scoreinc, 'bracketleft')
wn.onkeypress(scoredec, 'bracketright')

wn.onkeypress(mute, 'comma')
wn.onkeypress(unmute, 'period')

wn.onkeypress(toggle_keyset, "slash")

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
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)
    
        # Add a segment
        # But not yet, we'll get to that a bit later

          # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment = turtle.Turtle('image_sample2')
        
        new_segment.color("grey")
        new_segment.penup()
        if is_muted == False:
            #playsound(f'{p}/sounds/rip.wav', True)
            pygame.mixer.Sound.play(s_rip)
        
        # Add our segment to the list
        segments.append(new_segment)
        if is_muted == False:
            #playsound(f'{p}/sounds/boom.wav', True)
            pygame.mixer.Sound.play(s_boom)

        # Let's make our snake go a little faster by shortening delay some
        delay -= 0.003
        if delay < 0: 
            delay = 0

        # Add 10 to our score
        score += 1

        # If our new score is > high_score, we have a new high score
        if score > high_score:
            high_score = score
        
        

         # Update score display
        pen.clear()
        pen.write(f"IQ : {score}  poverty: {high_score}", align="center",
            font=("Comic Sans MS",40,"bold"))
       
    # Move our head turtle if it has some direction set
    move()
    
      # Check to see if head is too close to any segment
    for segment in segments:
        if segment.distance(head) < 20:
            if is_muted == False:
                #playsound(f'{p}/sounds/screamed.wav', True)
                pygame.mixer.Sound.play(s_screamed)
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
            set_high_scores()

            score = 0
            
            # Reset delay
            delay = 0.1
            
            # Update score
            pen.clear()
            pen.write(f"IQ : {score} poverty : {high_score}", align="center",
                font=("Comic Sans MS",40,"bold"))

                 # Check for too close to a wall
    # We'll count anything within 10px of any edge as a hit
    # Since our window is assumed to be 600x600 and center is 0,0
    #   our boundaries are:
    #   Left side = -(600/2)+10
    #   Right side = (600/2)-10
    #   Etc. - For now, these numbers are fine.
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        if is_muted == False:
            #playsound(f'{p}/sounds/scary.wav', True)
            pygame.mixer.Sound.play(s_scary)
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        if is_muted == False:
            #playsound(f'{p}/sounds/oof.wav', True)
            pygame.mixer.Sound.play(s_oof)
        set_high_scores()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"IQ : {score}  poverty : {high_score}", align="center",
            font=("Comic Sans MS",40,"bold"))

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
        segments[0].hideturtle()
    
    image_change()

    time.sleep(max(.0001,delay))

