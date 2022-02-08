import turtle;
import collections;

tr = turtle.Turtle();
wn = turtle.Screen();
wn.addshape("hangman.gif");
tr.shape("hangman.gif");
guessedlatters = '';
def waitforkeypress():
    input('');
def printturtle(x, y, fontsize, message):
    turtle.up();
    turtle.ht(); # hide turtle, might not work
    turtle.goto(x,y);
    turtle.write(message,font=("Arial",fontsize,"normal"));
secretword = turtle.textinput("enter secret word","word");
secretwordlist = list(secretword);
gamewordlist = ['_', '_', '_', '_', '_'];
gameover = False;
numberofguesses = 0;
notinword = '';
wn.addshape('hangman.gif');
tr.shape('hangman.gif')
while not(gameover or numberofguesses>6):
    printturtle(-150,80,30,gamewordlist);
    guessedletter=turtle.textinput("enter","letter");
    printturtle(-150,80,30,gamewordlist);
    if (guessedletter in secretwordlist):
        for i in range(0, 5):
            if guessedletter == secretwordlist[i]:
                gamewordlist[i] = guessedletter;
                printturtle(-150,80,30,gamewordlist);
    else:
        printturtle(-150,80,30,gamewordlist);
        numberofguesses +=1;
        notinword+=guessedletter;
        printturtle(-150, -125,30,"lettrers not in word");
        printturtle(-150, -170, 30, notinword)
    turnsleft = 7-numberofguesses;
    printturtle(-150,-205,30,"turns left below");
    printturtle(-185+35*numberofguesses,-240,30,str(turnsleft))
    if numberofguesses == 1:
        wn.addshape("hangman2.gif");
        tr.shape("hangman2.gif")
    if numberofguesses == 2:
        wn.addshape("hangman3.gif")
        tr.shape("hangman3.gif")
    if numberofguesses == 3:
        wn.addshape("hangman4.gif");
        tr.shape("hangman4.gif")
    if numberofguesses == 4:
        wn.addshape("hangman5.gif");
        tr.shape("hangman5.gif")
    if numberofguesses == 5:
        wn.addshape("hangman6.gif");
        tr.shape("hangman6.gif")
    if numberofguesses == 6:
        printturtle(-150,-280,30,"you lost");
        wn.addshape("hangman7.gif");
        tr.shape("hangman7.gif");
        gameover = True;
    if collections.Counter(gamewordlist)==collections.Counter(secretwordlist):
        printturtle(-150,40,30,"you won!");
        gameover = True;
    printturtle(-150,80,30, gamewordlist)
wn.mainloop()
