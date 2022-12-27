cars = 100
#This is the number of cars
space_in_a_car = 4.0
#The number of passengerrs that a car can fit
drivers = 30
#The number of drivers available today
passengers = 90
#The number of passengers who need to be transported today
cars_not_driven = cars - drivers
#The number of total cars available minus drivers, giving the unused cars
cars_driven = drivers
#Each driver will drive one car
carpool_capacity = cars_driven * space_in_a_car
#The number of cars being used multiplied by the number of passengers that Will
#fit. Giving the total number of passengers the company can handle
average_passengers_per_car = passengers / cars_driven
#The number of passengers who need rides divided by the number of cars driven
#This determines if the company will be within capacity
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
