""" Silent Auction program. This program gets a product and reserve price, then runs a silent auction, recording the name and bid
of the highest bidder. Once -1 is entered for the bid, the auction ends and the winner is displayed. """

# get the item name and reserve price
item_name = input("Enter the item name: ")
# make sure we get a valid reserve price
get_reserve = True
while get_reserve == True:
    try:
        reserve = float(input("Enter the reserve price: "))
        get_reserve = False
    except:
        print("Reserve price must be a number.")

# set variables for the current highest bidder and highest bid.
highest_bidder = ""
highest_bid = 0

# set boolean to True so bidding process repeats until -1 is entered
keep_bidding = True

# start auction
while keep_bidding == True:
    name = input("Enter your name: ")
    # error check to make sure we get a float for the bid
    get_bid = True
    while get_bid == True:
        try:
            bid = float(input("Enter your bid: "))
            get_bid = False
        except:
            print("Bid must be a number.")
    # check if -1 has been entered for the bid as this will end the auction
    if bid == -1:
        keep_bidding = False
    # check if bid is higher than the current highest bid. If so, change name of highest bidder and value of highest bid
    elif bid > highest_bid:
        highest_bidder = name
        highest_bid = bid
    else:
        print("Please enter a higher bid")
    print("The current highest bidder is {}, with a bid of {}".format(highest_bidder, highest_bid))

# check if the highest_bid has exceeded the reserve price
if highest_bid >= reserve:
    print("The auction for the {} has finished. The winner is {}, with a bid of ${}".format(item_name, highest_bidder, highest_bid))
else:
    print("The reserve price of ${} has not been met, so the {} will not be sold today.".format(reserve, item_name))