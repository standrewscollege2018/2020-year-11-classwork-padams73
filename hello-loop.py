""" This program demonstrates a for loop with a variable. It asks the user how many times to repeat. """

# ask how many names the user will enter

number = int(input("How many names do you wish to enter? "))

# repeatedly ask for names and greet them
for i in range(0, number):
    name = input("Enter a name: ")
    print("Hello", name)
    

             