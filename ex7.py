print("Mary had a little lamb.")
#The entire string is written with the .format() at the end.
#The {} could be anywhere on the string and 'snow' would be Added
#Adding multiple {} will cause an error. Guessing there is a way to add multiple
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) #what'd that do?
#It printed 10 periods

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch end = ' ' at the end. Try removing it to see what happens
#Adding the end=' ' combines the two printed words on the same line with a space
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

#Removing the end=' ' will make it say Cheese Burger (each word on different line)