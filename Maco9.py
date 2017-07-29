#guessing game

import random
myNum = random.randint(1, 10)

print("Guess my number between 1-10. Beware, you only have three chances:")

max_guesses = 3

guessesLeft = max_guesses
while guessesLeft:
    print("take a guess")
    guess = int(input("Guess:"))


    guessesLeft -= 1

    if guess == myNum:
        print("Gold stars for everyone!")
    elif (guess == myNum - 1) or (guess == myNum + 1):
        print("Your on fire!!")
    elif (guess == myNum - 2) or (guess == myNum + 2):
        print("close but no cigar")
    elif guess != myNum:
        print("HA HA Good try")
    if guessesLeft == 0:
        print("You are out of guesses. The number was", myNum)