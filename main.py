for i in range(0,3):
    j="true";
    if j=="true":
        if j == "true":
            if j == "true":
                print("welcome to division problem number " + str(i));
                dividend = int(input("Please enter a dividend"));
                divisor = int(input("Please enter a divisor"));
                quotient = dividend // divisor;
                remainder = dividend % divisor;
                print(str(dividend) + " divided by ",str(divisor) + " is " + str(quotient) + ", with a remainder of " + str(remainder));
