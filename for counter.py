""" This program gets two numbers from the user, then counts up from the lower to the higher. """

number_1 = int(input("Enter a number"))
number_2 = int(input("Enter another number"))

if number_1 < number_2:
    start = number_1
    stop = number_2
else:
    start = number_2
    stop = number_1

for i in range(start, stop+1):
    print(i)

print("All done")