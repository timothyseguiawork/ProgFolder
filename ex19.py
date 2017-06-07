# Exercise 19: Functions and Variables
# 06/07/2017

# The variables in your function are not connected to the variables in your script.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly: "
cheese_and_crackers(20,30)

print "Or we can use variables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math: "
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# This shows all the diff ways we're able to give our function "cheese_and_crackers"
#   the values it needs to print them.

# Study Drills
# 1 Go back through the script and type a comment above aech line explaining in english what it does.
# 2 Start at the bottom and read each line backward saying all the important characters.
# 3 Write at least one more function of your own design and run it 10 different ways. 
