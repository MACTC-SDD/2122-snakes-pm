
import turtle
import time
import random
import requests

delay = 0.1
score = 0
high_score = 0
boost = 0

game_title = ' (Julius)'
hs_link = 'http://api.snakegame.cf/scores'
player_name = "???"

wn = turtle.Screen() 
wn.title("Snake Game")
wn.bgcolor("green")

wn.setup(width=1200, height=900)
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
colors = random.choice(['red', 'blue', 'black'])
shapes = random.choice(['square','triangle','circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0,250)

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

def speed_boost():
    global boost
    if boost == 0:
        boost = .09
        head.color ("purple")


def move():
    if head.direction == "up":
        y = head.ycor()
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

def update_score():
    pen.clear()
    pen.write(f"Score : {score}  High Score : {high_score}", align="center",
        font=("candara",24,"bold"))

def reset():
    global delay
    global score
    global segments

    # Save score to leaderboard
    try:
        data=f'"name": "{player_name}", "score": "{score}", "game": "{game_title}"'
        data = '{' + data + '}'
        r = requests.post(f'{hs_link}', headers={'Content-Type': 'application/json'}, data=data)
    except:
        print(f'Failed to post high score: {r.status_code}')

    delay = .1
    score = 0
    segments.clear()

wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
wn.onkeypress(speed_boost, "space")

segments = []

while True: 
    wn.update()
    if head.distance(food) < 20:
        x = random.randint(-370,370)
        y = random.randint(-370,370)
        food.goto(x,y)
        delay -= 0.001
        score += 10
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        segments.append(new_segment)
        update_score()
        if score > high_score:
            high_score = score


    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"    
            for segment in segments:
                segment.goto(1000,1000)
            reset()
            update_score()
    if head.xcor() > 600 or head.xcor() < -600 or head.ycor() > 450 or head.ycor() < -450:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            reset()
            update_score()   
    time.sleep(max(.001,delay - boost))
    if boost > 0:
        boost = max(0,boost - .01)
    else:
        head.color("white")
    print(boost)
