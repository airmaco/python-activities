#greeting questions V1

def greeting():
    name = input("please enter your name: ")
    print("nice to meet you",name)
    print(name, end="")
    color= input(",What is your favorite color: ")
    print( color, end="")
    print("? That's a nice color.")
    print(name, end="")
    food= input(", what is your favorite food: ")
    print(food, end="")
    print(" sounds yummy")
    print(name, end="")
    gotoGo= input(", do you gave to leave? (yeah/nah)")
    if(gotoGo == "yes"):
        print("Goodbye", name)
    else:
        greeting()

greeting()

