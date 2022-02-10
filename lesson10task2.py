creator = "notlassen";
def greet(name,house):
    if creator == "notlassen":
        print(f"Hello {name}! nice to meet you!")
        if house=="hess":
            print("we are in the same house")
        elif house != "hess":
            print("we are not in the same house");
greet("Christian","hess")
greet("Remy","ershig");
