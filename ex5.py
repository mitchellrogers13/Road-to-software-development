name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
height_in_cm = height * 2.54
weight = 180 #ibs
weight_in_kg = weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about  {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_in_cm} centimeters tall in Europe.")
print(f"His height in cm can be rounded to {round(height_in_cm)} centimeters.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_in_kg} kilograms heavy for some reason.")
print(f"His weight in kg can be rounded to {round(weight_in_kg)} kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {teeth} depending on the coffee.")

#This line is tricky. Try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
