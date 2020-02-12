""" This program calculates how much a movie ticket is for you """

#are they a student
student_status = input("Are you a student y/n")


#give them their price
if student_status == "y":
    print("Ticket price is $8")
else:
    #get the user age
    user_age = int(input("What is your age"))
    if user_age >=18:
        print("The price is $12")
    elif user_age >= 13:
        print("the price is $9")
    elif user_age >= 5:
        print("The price is 79")
    else:
        print("The price is free")