""" This program demonstrates how lists work, including how to print, change and append items. """

# lists always have square brackets. Items are separated by commas
fruit = ["Apples", "Oranges", "Kiwifruit", "Bananas"]

# To print an item from a list, we use the name of the list and its index (which starts at 0)
print(fruit[3])
# you can print out the entire list
print(fruit)
# len(list()) gives the number of items in the list
print(len(fruit))

# to change an item, just use its index and set it directly
fruit[0] = "Mango"
print(fruit)
# To insert an item at a specific location, use insert(index, item)
fruit.insert(3, "Apples")
print(fruit)
# often it's easier to just add a new item to the end of list
# to do this, we use append()
fruit.append("Guava")
print(fruit)
