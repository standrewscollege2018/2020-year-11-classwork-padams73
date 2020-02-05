""" This program converts gigabytes into megabytes. It demonstrates use of a constant and the .format() function. """

# Set the number of megabytes in a gigabyte
MB = 1024

# get the number of gigabytes from the user
gb = int(input("How many gigabytes?"))

# print out the answer
print("There are {} megabytes in {} gigabytes".format(gb*MB, gb))