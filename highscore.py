""" Testing to see how to read and write to csv files. 
This program reads the high score and name from a text file called highscore.txt. The text file is in the same folder as this program.
The text file has the format:
score, name
e.g. 5, John

The program knows that the two bits of information are separated by a comma, so can grab each individually and assign to variables. 

When writing a new high score back into the text file, we set the mode to 'w', and use writerow() to write the data over the top of the 
existing information. """


# import the csv package
import csv

# open the highscore.text file, calling it csv_file
with open('highscore.txt') as csv_file:
    # set up csv_reader as a multi-dimensional list with a row for each score (1 in our example), and information separated by commas
    csv_reader = csv.reader(csv_file, delimiter=',')
    # loop through the csv_reader list and pull out the high score and the name
    for row in csv_reader:
        # high score is the first position in the row, so we use row[0]. It is a string so we change it to an integer using int()
        high_score = int(row[0])
        name = row[1]
        # we need to break out of the loop to avoid errors as when writing a line break is always added
        break

# display the current high score details
print("Current high score: {} ({})".format(high_score, name))

# get the user to enter their new score
new_score = int(input("Enter new score: "))
# if it is higher than the current high score that we pulled from the text file, we tell them and get their name
if new_score > high_score:
    print("New high score!")
    new_name = input("Enter your name:")
    # open highscore.txt again, this time in write mode
    with open('highscore.txt', mode='w') as csv_file:
        # set up the writer, telling it to use a comma between the variables being written
        score_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        # write a new row over the existing one
        score_writer.writerow([new_score, new_name])    
else:
    print("Bad luck, not a new high score")
