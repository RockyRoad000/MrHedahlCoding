import turtle;

r = 255;
g = 0;
b = 0;

mode = 0;

colorspeed = 2;

turtle.colormode(255);
turtle.turtlesize(10);
turtle.shape("turtle");

while 0 == 0:

    if r >= 254:
        mode = 1;
    elif g >= 254:
        mode = 2;
    elif b >= 254:
        mode = 3;

    if mode == 0:
        mode = 1;
    elif mode == 1:
        r-=colorspeed;
        g+=colorspeed;
    elif mode == 2:
        g-=colorspeed;
        b+=colorspeed;
    elif mode == 3:
        b-=colorspeed;
        r+=colorspeed;

    turtle.color(r,g,b);

