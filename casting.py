""" Demonstrating why we use casting to set the data type of inputs. """

# get numbers from the user
number = input("Enter a number")

# print double the number
print("Double {} is {}".format(number, number*2))


# get number as an integer
number_int = int(input("Enter another number"))

# print double the number
print("Double {} is {}".format(number_int, number_int*2))