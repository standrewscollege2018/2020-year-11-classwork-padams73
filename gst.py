""" This program gets an item name and price, then adds GST to the price. """

# Set the gst to 15%
# Because gst is a constant (doesn't change, we name it in uppercase
GST = 0.15

# get the name and price
item_name = input("Item name?")
item_price = float(input("Item price?"))

# print the name and price including GST
print("The", item_name, "will cost", item_price * (1 + GST), "including GST")