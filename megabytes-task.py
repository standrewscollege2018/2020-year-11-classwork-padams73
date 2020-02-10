""" This is my madlib program where we are using varables and inputs and outputs to form a sentance """ 

#Inputs for the madlib

name = input("Enter a name")
subject = input("Enter a class")
reason = input("Enter a reason")
whofrom = input("Enter who from") 
time = input("Enter when they are coming back")

#Madlib is thinking
print("Thinking.... Here's my madlib")

#Text for the sentence 

print("To whom it may concern,\n Please excuse {} from{} today. He is suffering from a bad case of the{} which has been caused by the{}.{} should recover and be\
back at school{}. \n Kind regards \n{}'s Turtle.".format(name, subject, reason, whofrom, name, time, name)) 
