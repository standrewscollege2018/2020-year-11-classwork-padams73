""" Car rental program - Achieved exemplar.
This program asks the user for the number of seats required and then displays all vehicles, regardless of how many seats they
have or whether they are available. The user can then select the number of the car they want, which then changes the car to unavailable.
The program continues until the user enters 0 for the number of seats required, at which point it displays a list of the cars, with their
availability.

This is Achieved because it will only work as intended if the user gives expected inputs. There is no error-catching and comments are minimal."""

# separate lists with car details including: name, number of seats, availability
cars = ["Suzuki van", "Toyota Corolla", "Honda CRV", "Suzuki Swift"]
seats = [2, 4, 4, 4]
availability = [True, True, True, True]

# start loop running the program
run_program = True

while run_program == True:
    # Get the number of seats required
    seats_required = int(input("How many seats do you need? (0 to end program)\n"))
    # if user enters 0 it ends the program
    if seats_required == 0:
        run_program = True
        break
    # Loop through the lists and display the details for each car
    for i in range(len(cars)):
        print("{}. {} - Seats: {} - Availability: {}".format(i+1, cars[i], seats[i], availability[i]))
        # If a car doesn't have enough seats, display a warning
        if seats[i] < seats_required:
            print("NOT ENOUGH SEATS")
    # Get the user to choose which car they want to rent
    selection = int(input("Which number car do you want?\n"))
    # Change the availability of the selected car to False
    availability[selection-1] = False

# Display list of booked cars
print("Booked cars")
print("-----------")
# check if availability is False, if so then print the name of the car
for i in range(len(cars)):
    if availability[i] == False:
        print(cars[i])
                         
                         
