inputs =[
    "enter your name",
    "enter a favorite snack",
    "enter a positive number",
    "enter a color",
    "enter a shape",
    "enter one of your favorite hobbies",
    "enter a day of the week",
    "enter a time of day",
    "enter a different day of the week"
]

for i in range(0, len(inputs)):
    inputs[i] = input(inputs[i])

print(f"\nmy name is {inputs[0]}, I like to have {inputs[2]} {inputs[1]}s every day for snack")
print(f"my favorite shape is {inputs[3]} {inputs[4]}, which have {int(inputs[2])+3} sides")
print(f"One of my favorite hobbies is {inputs[5]} on {inputs[6]} at {inputs[7]}, but not on {inputs[8]}")
