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
guesses = 1

while guesses < 6 and guess != number:
    if guess > number:
        print("That guess was too high!")
    else:
        print("That guess was too low!")
    guess = int(input("What's your next guess? "))
    guesses = guesses + 1

if guess == number:

    #
    # Tell them they are the best so they'll want to play again.
    print("You got it right! Great job.")

else:

    #
    # Throw them some shade so they'll want to play again.
    print("Oh, so sorry. You ran out of guesses.")
    print("The number was "+str(number)+".")
    print("Maybe my telepathic skills are on the fritz.")
