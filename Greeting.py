#V2 greeting questions

print("this is where version 2 starts")
gotoStart = "no"
while gotoStart == "no":
    name = input ("please enter your name: ")
    print("Nice to meet you", name)

    color = input(", what is your favorite color: ")
    print(color, "? thats a nice color")
    food = input(", what is your favorite food: ")
    print(food, "sounds yummy.")
    gotoStart = input(", do you have to leave (yes/no)")
print("goodbye")
