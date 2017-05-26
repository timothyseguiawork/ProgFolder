# Exercise 11 & 12: Asking Questions & Prompting People
# 05/26/17

# Most of what software does is the following
# 1. Take Some kind of input from a person
# 2. Change it
# 3. Print out something to show how it changed

# So far you have been printing strings, but you haven't been able to get any input from anyone
# You may not even know what "input" means so type in those code and find out what it does

# print "How old are you?",
# age = raw_input()
age = raw_input("How old are you? ")
x = int(raw_input("Input a value for x: "))
y = int(raw_input("Input a value for y: "))
print "%d + %d = %d" % (x, y, x+y)
# print "How tall are you?",
# height = raw_input()
height = raw_input("How tall are you? ")

# print "How much do you weigh?",
# weight = raw_input()
weight = raw_input("How much do you weigh? ")

print "So, you're %r years old, %r tall, and %r heavy." % (age, height, weight)
