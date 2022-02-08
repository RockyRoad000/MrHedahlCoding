import turtle
import random
import time
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.speed(speed='fastest')
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

turtle.clearscreen()
turtle.bgcolor('black')
t2 = turtle.Pen();
t2.speed(speed='fastest')

def draw(n, x, angle):
    # loop for number of stars
    for i in range(n):

        turtle.colormode(255)

        # choosing random integers
        # between 0 and 255
        # to generate random rgb values
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)

        # setting the outline
        # and fill colour
        t2.pencolor(a, b, c)
        t2.fillcolor(a, b, c)

        # begins filling the star
        t2.begin_fill()

        # loop for drawing each star
        for j in range(5):
            t2.forward(5 * n - 5 * i)
            t2.right(x)
            t2.forward(5 * n - 5 * i)
            t2.right(72 - x)

        # colour filling complete
        t2.end_fill()

        # rotating for
        # the next star
        t2.rt(angle)


# setting the parameters
n = 30  # number of stars
x = 144  # exterior angle of each star
angle = 18  # angle of rotation for the spiral

draw(n, x, angle)
turtle.delay(1000);
turtle.clearscreen()
turtle.bgcolor('black')
draw(30,72,9)
turtle.delay(1000)

turtle.clearscreen()
turtle.bgcolor('black')

t3 = turtle.Pen()
t3.speed(0)
t3.color("yellow")
t3.pencolor("red")
t3.begin_fill()
time_1 = time.time()
while True:
    t3.forward(200)
    t3.left(170)
    if time.time() - time_1 > 1.4:
        print("time", time_1 - time.time(), "time should be 1.4")
        break;


t3.end_fill()
turtle.delay(1000)

turtle.clearscreen()
turtle.bgcolor('white')

t4 = turtle.Pen();
t4.speed(0);
for i in range(0,23):
    t4.circle(5*i)
    t4.circle(-5*i)
    t4.left(i)


turtle.delay(1000)
turtle.clearscreen()
turtle.bgcolor('lightgreen')
t5 = turtle.Pen()
t5.color('blue')
t5.speed(0)

def drawSquare(t, sz):
    for i in range(4):
        t.fd(sz)
        t.left(90)

def drawGrid(t, sz):
    for i in range(4):
        drawSquare(t, sz)
        t.left(90)

for i in range(5):
    drawGrid(t5, 100)
    t5.left(18)

turtle.delay(1000)
turtle.clearscreen()
turtle.bgcolor('mintcream')
t6 = turtle.Pen()
t6.color('blue')
t6.speed(0)
for i in range(0,650):
    t6.forward(2+i);
    t6.right(80.899)


turtle.clearscreen()
turtle.bgcolor('black');
draw(30,72,40)


turtle.done()
