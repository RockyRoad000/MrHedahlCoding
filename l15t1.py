from random import *;
player1score = 10;
while player1score>=0:
    print("player1, please roll your dice");
    die1 = randint(1,6); # fix later because die1 and die2 will always be the same
    die2 = randint(1,6); # fix later because die1 and die2 will always be the same
    total=die1+die2;
    print(die1, die2, total);
    if total%2 == 0:
        player1score = player1score+10;
        print("well done, you have an even total, 10 points have been added to your score.");
        print("your total is",player1score);
    else:
        player1score = player1score-10;
        print("your have an odd total, 10 points have been subtracted from your score.\"\"");
        print("your total is",player1score)



