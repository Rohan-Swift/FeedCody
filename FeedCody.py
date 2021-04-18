import turtle
import time
import random
import winsound
 
delayM = 0.1
delay=delayM
delayChangeM = 0.001
delayChangeS = delayChangeM
 
# Score
score = 0
high_score = 0
 
#Screen
wn = turtle.Screen()
wn.title("Snake Game")
winsound.PlaySound('Sea.wav',winsound.SND_ASYNC)
#wn.bgcolor("#add8e6")
wn.bgpic("background.gif")
wn.addshape('cody.gif')
wn.addshape('bonusf.gif')
wn.addshape('byte.gif')
wn.setup(width=585, height=585)
wn.tracer(0) # Turns off the screen updates
 
# Crab head
head = turtle.Turtle()
head.speed(0)
head.shape("cody.gif")
head.penup()
head.goto(0,0)
head.direction = "stop"
 
# Crab food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
 
segments = []
 
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
 
# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
 
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
 
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
 
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
 
# Main game loop
while True:
    wn.update()
 
    if score >= 0:
        #here you would do something once it passes 50. You can also modify it to only pass this condition once.
    # Check for a collision with the border
     if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.speed(0)
        food.shape("circle")
        food.color("red")
        food.penup()
        food.goto(x,y)
        delayM = 0.1
        delay=delayM
        delayChangeM = 0.001
        delayChangeS = delayChangeM
        head.speed(0)
        head.shape("cody.gif")
        head.penup()
        head.goto(0,0)
        
        
 
         #Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
         #Clear the segments list
        segments.clear()
 
         #Reset the score
        score = 0
 
        # Reset the delay
        delay = delayM
        delayChangeS=delayChangeM
 
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
 
 
    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)
 
        if score >= 30:
            #food = turtle.Turtle()
            food.speed(0)
            food.shape("bonusf.gif")
            food.penup()
            food.goto(x,y)
            if score >= 60:
                delayM = 0.06
                delay=delayM
                delayChangeM = 0.0009
                delayChangeS = delayChangeM
                if score >= 90:
                    #creating Shark obstruction
                    head.speed(0)
                    head.shape("byte.gif")
                    head.penup()
                    head.goto(0,0)        




        # Add a segment
        #new_segment = turtle.Turtle()
        #new_segment.speed(0)
        #new_segment.shape("square")
        #new_segment.color("grey")
        #new_segment.penup()
        #segments.append(new_segment)
 
        # Shorten the delay
        delay -= delayChangeS
 
        # Increase the score
        score += 10
 
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
 
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
 
    move()    
 
    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()
 
            # Reset the score
            score = 0
 
            # Reset the delay
            delay = delayM
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
 
    time.sleep(delay)
 
wn.mainloop()