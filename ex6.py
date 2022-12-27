#defining a variable to equal 10
types_of_people = 10
#setting x equal to a formatted string that includes the first variable
x = f"There are {types_of_people} types of people."
#Setting a variable equal to a simple string
binary = "binary"
#Setting a variable equal to a simple string
do_not = "don't"
#Setting a variable equal to a formatted string that includes the prior two
#variables
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"If I said: {x}")
#Added quotes around {y} to improve sentence structure
#I also said: 'Those who know binary and those who don't.'
print(f"I also said: '{y}'")

hilarious = False
#Leaving the {} allowed me to format a variable into that space
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#Can add strings together using +
print(w + e)
