""" This program demonstrates if statements using child age for zoo entry """

# Set the child age limit
CHILD_AGE = 13

# Get the age from the user
# Use int() so we can compare to CHILD_AGE
age = int(input("How old are you?\n"))

# check if user is a child or not
if age < CHILD_AGE:
    print("You pay the child price!")

# print welcome
print("Welcome to the zoo")
