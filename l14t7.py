secretword = "python";
# secret word should not have any spaces in it, because then you will have to guess the space key
temp = "";
guessedword = temp.zfill(len(secretword));
guess = -1;
print(guessedword)
x = y = guessnum = 0;
while x==y:
    guess=input("guess a letter, it is in a " + str(int(len(secretword))) + " letter word");
    for i in range(0, len(secretword)):
        if guess == secretword[i]:
            print("correct, position",abs(0-i)-(0-1)," (position starting at position 1)")
            temp = list(guessedword)
            temp[i]=guess
            guessedword = "".join(temp)
    print("so far your guess is",guessedword+".","Zeros are things you have not yet guessed\n")
    guessnum+=1;
    if guessedword == secretword:
        print("guessed the word fully");
        print("it took " + str(guessnum) + " guesses for you to correctly guess a " + str(int(len(secretword))) + " letter word")
        break;
