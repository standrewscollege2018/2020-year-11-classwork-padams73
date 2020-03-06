""" Car rental program - Excellence exemplar.
This program asks the user for the number of seats required and then displays all vehicles, regardless of how many seats they
have or whether they are available. The user can then select the number of the car they want, which then changes the car to unavailable.
The program continues until the user enters 0 for the number of seats required, at which point it displays a list of the cars, with their
availability.

This is Excellence because it uses efficient data storage (nested lists), commenting is detailed, and there is comprehensive
error-catching that ensures that the program handles unexpected, boundary and invalid inputs."""

# list of all vehicles. Each sub-list contains the name of the car, number of seats and whether it is available
cars = [["Suzuki van", 2, True], ["Toyota Corolla", 4, True], ["Honda CRV", 4, True], ["Suzuki Swift", 4, True]]

# start the program running. run_program is a Boolean that will keep the program running as long as it is True
run_program = True

while run_program == True:
    # get the number of seats required by the user. Error check to make sure we get valid input
    get_seats = True
    while get_seats == True:
        # using try and except to make sure our program can handle invalid inputs like string or float when we want an integer
        try:
            # get the number of seats required
            seats_required = int(input("How many seats are required? (Enter 0 to end the program)\n"))
            # if user enters a negative number we print an error and ask again
            if seats_required < 0:
                print("Enter a number greater than zero")
            else:
                # if we get a positive integer we stop asking and move on in the program
                get_seats = False
        except:
            print("Enter a positive integer")
            
    # check if user entered 0. If so, stop running the program
    if seats_required == 0:
        run_program = False
        break
    
    # display a numbered list of the cars, the number of seats, and whether they are available
    for i in range(len(cars)):
        print("{}. {} - Seats: {} - Available: {}".format(i+1, cars[i][0], cars[i][1], cars[i][2]))
        # if a car doesn't have enough seats for the user, we print an alert so that they don't book it
        if seats_required > cars[i][1]:
            print("NOT ENOUGH SEATS")
            
    # now we get the number of the car the user wants to book        
    get_selection = True
    # repeatedly ask the user for the number of the car they want until they give a valid number
    while get_selection == True:
        # using try and except to ensure we get a valid number
        try:
            # get number of car from the user
            selection = int(input("Enter number of car\n"))
            # first we check to see if they enter a number in the correct range
            if selection not in range(1,len(cars)+1):
                print("Please enter a number between 1 and {}".format(len(cars)))
            # next we check to see if the car is actually available and has enough seats. If not, print an alert
            elif cars[selection-1][2] == False or cars[selection-1][1] < seats_required:
                print("You can't book this vehicle")
            # if we get valid input, change the availability of the selected car to False
            else:
                cars[selection-1][2] = False
                # set get_selection to False so we can move on in the program
                get_selection = False
        except:
            print("Enter a valid number between 1 and {}".format(len(cars)))

# When the program finishes running we print a list of all the cars that have been booked.
print("Booked cars")
# cars_booked is a variable that stores the number of cars that have been booked today
cars_booked = 0
# loop through the list of cars and check if availability is False for each one
for i in range(len(cars)):
    if cars[i][2] == False:
        # if availability is False, car has been booked so we print its name
        print(cars[i][0])
        # add 1 to the numbers of cars booked
        cars_booked += 1
# handle the boundary case where the programs ends with no cars being booked. If cars_booked equals zero we print No cars booked today.
if cars_booked == 0:
    print("No cars booked today")