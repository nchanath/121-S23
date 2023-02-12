import random

#
# Greet them in a spectacular way.
splash = "AWESOME CSCI 121 GUESSING GAME"
print()
print("*"*(len(splash)+4))
print("* "+splash+" *")
print("*"*(len(splash)+4))
print()

#
# Pick a random number from 1 to 100.
number = random.randint(1,100)

#
# Ask them to guess it.
print("I have chosen a random number from 1 to 100.")
print("Try and guess what it is.")
print()

guess = int(input("Your guess? "))
while guess != number:
    if guess > number:
        print("That guess was too high!")
    else:
        print("That guess was too low!")
    guess = int(input("What's your next guess? "))

#
# Tell them they are the best.
print("You got it right! Great job.")



    
        
