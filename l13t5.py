def main():
    print("Contracts Manager");

    #initialize friends list
    pets =[
        []
    ]
    infile = open("contracts.txt","a"); # uses a for append instead of r so the file will be automatically created
    infile.close();
    infile = open("contracts.txt","r"); # uses rw instead of r so the file will be automatically created
    line=infile.readline();
    while line:
        petTemp = line.rstrip("\n").split(",")
        pets.append(petTemp)
        line=infile.readline();
    infile.close();
    choice = 0;
    while choice !=4:
        print("1) Add Pet");
        print("2) Look up a pet");
        print("3) Display all pets");
        print("4) Quit")
        choice = eval(input());

        if choice == 1:
            print("Adding a pet");
            name = input("Enter name: ");
            email = input("Enter when you got the pet: ");
            phone = input("Enter Type of pet: ");
            pets.append([name,email,phone]);
        elif choice == 2:
            print("Look up a pet");
            keyword=input("enter search term:");
            for i in range(0,len(pets)):
                for pet in pets[i]:
                    if keyword in pet:
                        print(pet);
        elif choice == 3:
            print("Displaying all pets");
            for i in range(len(pets)):
                for j in range(len(pets[i])):
                    print(pets[i][j],end="");
                    if int(j)!=2:
                        print("",end=", ")
                print("\n",end="")
        elif choice == 4:
            print("Quitting program");
        else:
            print("unknown response");
    print(choice);
    outfile = open("contracts.txt", "w");
    for pet in pets:
        outfile.write(",".join(pet)+"\n")
    outfile.close();
    print("written to file \"contracts.txt\" succesfully")
main();

# save data to external file
print("program terminated");
