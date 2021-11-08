for i in range(1,100):
    if i % 7 == 0 and i % 3 == 0:
        print( str(i) + " BONUS");
    elif i%7 == 0 and i%3 != 0:
        print(str(i)+" is divisible by 7");
    elif i %3 == 0 and i%7 !=0:
        print(str(i)+" is divisible by 3");
    else:
        print(str(i) + " is not divisible by three or seven without a remainder")
