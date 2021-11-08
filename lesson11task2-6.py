print("task 1:")
for i in range(0,6):
    for j in range(1,i):
        print(f"{j:>4}",end='')#f string to format
    print()
print("task 2:")
for i in range(2,6):
    for j in range(0,i):
        print(f"{j:>4}",end='')#f string to format
    print()

print("task 3:")
for i in range(1,12,2):
    for j in range(2,i,2):
        print(f"{j:>4}",end='')#f string to format
    print()

print("task 4:")
for i in range(6,-1,-1):
    for j in range(1,i,1):
        print(f"{j:>4}",end='')#f string to format
    print()

print("task 5:")
for i in range(0,5,1):
    for j in range(5,i,-1):
        print(f"{j:>4}",end='')#f string to format
    print()

print("task 6:")
for i in range(5,-1,-1):
    for j in range(5,i,-1):
        print(f"{j:>4}",end='')#f string to format
    print()
