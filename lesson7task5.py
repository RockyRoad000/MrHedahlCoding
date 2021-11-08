for i in range(0,100):
    if i%3 ==0 and i%7 ==0:
        print()
    if i%3==0 and i%7 != 0:
        print(str(i) + " is divisible evenly by 3 but not 7")
    if i % 7 == 0 and i % 3 != 0:
        print(str(i) + " is divisible evenly by 7 but not 3")
