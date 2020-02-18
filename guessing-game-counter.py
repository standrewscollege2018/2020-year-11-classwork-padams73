""" This program generates a random number for the user to guess, then repeatedly asks them to guess, giving them hints. """

# import the random package
import random

# generate the random number to guess
number = random.randint(1,100)

# set a counter to record how many guesses it takes
counter = 0

# set Boolean variable so while loop will repeat until user guesses correctly
keep_asking = True

# start loop for guesses
while keep_asking == True:
    # add 1 to the counter
    counter += 1
    guess = int(input("Guess a number between 1 and 100\n"))
    if guess > number:
        print("Too high, guess again")
    elif guess < number:
        print("Too low, guess again")
    else:
        keep_asking = False

# print success message
print("That's right! It only took you {} guesses".format(counter))