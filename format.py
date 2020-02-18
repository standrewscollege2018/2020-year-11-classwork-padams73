""" This program demonstrates how the format() function works with print() """

# get the name and age of the user
name = input("Enter you name")
age = int(input("Enter your age"))

# print a message using print() only
print("Hello", name, "you are", age, "years old")

# print a message using print() and format()
print("Hello {}, you are {} years old".format(name, age))

