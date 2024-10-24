import turtle
import time
import random

# Constants
initial_delay = 0.15
delay = initial_delay
score = 0
high_score = 0
grid_size = 20
snake_speed = 20
score_multiplier = 1

# Set up the screen
wn = turtle.Screen()
wn.title("Hardest Snake Game Ever")
wn.bgcolor("#FFFFE0")
wn.setup(width=500, height=500)
wn.tracer(0)

# Draw the border around the game grid
def draw_border():
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("#4682B4")
    border_pen.pensize(5)
    border_pen.penup()
    border_pen.goto(-210, 210)
    border_pen.pendown()
    
    for _ in range(4):
        border_pen.forward(420)
        border_pen.right(90)
    border_pen.hideturtle()

# Draw the game grid
def draw_grid():
    grid_pen = turtle.Turtle()
    grid_pen.speed(0)
    grid_pen.color("#D3D3D3")
    grid_pen.penup()

    # Draw vertical lines
    for x in range(-200, 201, grid_size):
        grid_pen.goto(x, 200)
        grid_pen.pendown()
        grid_pen.goto(x, -200)
        grid_pen.penup()

    # Draw horizontal lines
    for y in range(-200, 201, grid_size):
        grid_pen.goto(-200, y)
        grid_pen.pendown()
        grid_pen.goto(200, y)
        grid_pen.penup()

    grid_pen.hideturtle()

# Snake head with alternating colors for unique style
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#006400")  # Dark green color for snake head
head.penup()
head.goto(0 + grid_size // 2, 0 + grid_size // 2)
head.direction = "stop"
head.shapesize(stretch_wid=1, stretch_len=1)

# Snake food with randomized appearance
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#FF4500")
food.penup()
food.goto(0 + grid_size // 2, 100 + grid_size // 2)
food.shapesize(stretch_wid=1, stretch_len=1)

segments = []

# Pen for score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("darkblue")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "bold"))

# Control functions for the snake
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

# Move the snake box-to-box with dynamic colors
def move():
    if head.direction == "up":
        head.sety(head.ycor() + grid_size)
    if head.direction == "down":
        head.sety(head.ycor() - grid_size)
    if head.direction == "left":
        head.setx(head.xcor() - grid_size)
    if head.direction == "right":
        head.setx(head.xcor() + grid_size)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Draw grid and border at the beginning
draw_grid()
draw_border()

# Main game loop
while True:
    move()

    # Check for collision with the border
    if head.xcor() > 190 or head.xcor() < -190 or head.ycor() > 190 or head.ycor() < -190:
        time.sleep(1)
        head.goto(0 + grid_size // 2, 0 + grid_size // 2)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = initial_delay
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))

    # Check for collision with the food
    if head.distance(food) < 20:
        x = random.randint(-190 // grid_size, 190 // grid_size) * grid_size + grid_size // 2
        y = random.randint(-190 // grid_size, 190 // grid_size) * grid_size + grid_size // 2
        food.goto(x, y)

        # Add a new segment to the snake with alternating colors
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(random.choice(["#32CD32", "#228B22", "#006400"]))  # Alternating green shades
        new_segment.penup()
        new_segment.shapesize(stretch_wid=1, stretch_len=1)
        segments.append(new_segment)

        score += 10 * score_multiplier
        score_multiplier += 0.1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(int(score), int(high_score)), align="center", font=("Courier", 24, "bold"))

        delay = max(0.05, delay * 0.95)

    # Move the end segments in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Check for collision with the body, but skip the first segment
    for segment in segments[1:]:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0 + grid_size // 2, 0 + grid_size // 2)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = initial_delay
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))

    wn.update()

    time.sleep(delay)
