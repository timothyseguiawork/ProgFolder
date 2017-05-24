#Exercise 4: Variables and Names
#100 cars
cars = 100
#400 spots
#space_in_a_car = 4 #leads to truncation of a number
space_in_a_car = 4.0 #no truncation becaues we use a floating point number
#1 driver per car
drivers = 30
#4 spots for 90 passengers
passengers = 90
#70 cars not driven
cars_not_driven = cars - drivers
#30 cars driven, without having to do math
cars_driven = drivers
#30*4 (120) spots for passengers
carpool_capacity = cars_driven * space_in_a_car
#general amt of passengers in a car
average_passengers_per_car = passengers / cars_driven

#surprising because concatenation already includes  spaces.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
