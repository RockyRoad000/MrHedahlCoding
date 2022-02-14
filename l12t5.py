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
       
    
    if r >= 255-colorspeed:
        mode = 1;
    elif g >= 255-colorspeed:
        mode = 2;
    elif b >= 255-colorspeed:
        mode = 3;

    turtle.color(r,g,b);

