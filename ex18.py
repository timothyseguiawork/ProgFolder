# Exercise 18: Names, Variables, Code, Functions
# 06/07/2017

# Functions do 3 things:
# 1 They name pieces of code the way variables name strings and numbers
# 2 They take arguments the way your scripts take argv
# 3 Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands"

# You can create a fuction by using the word "def" in Python. You will create 4 diff Functions
#   that work like scripts and then will be commented on how each one is related.

# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# OK, that *args is actually pointless, we can just do this.
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument.
def print_one(arg1):
    print "arg1: %r" % arg1

# This one takes no arguments.
def print_none():
    print "I got nothing."

print_two("Timothy", "Seguia")
print_two_again("Timothy", "Seguia")
print_one("First!")
print_none()

# Let's break down the first function, print_two
# 1 First we tell python we want to make a function using def for "define"
# 2 On the same line as def we give the function a name, in this case we called it print_two
#       but it could also be "peanuts". It doesn't matter, except that your function should have
#       a short name to reveal what it does.
# 3 Then we tell it we want *args (asterisk args) which is a lot like your argv parameter but for
#       functions. This hsa to go inside () to work.
# 4 Then we ned this line with a : (colon), and start indenting.
# 5 After the colon al the lines that are indented four spaces will become attached to this name,
#       pirnt two. Our first indented line is one that unpacks the arguments the same as with your scripts.
# 6 To demonstrate how it works we just print the arguments out, like we would in a script.

# Study Drills
# Create a function checklist for later exercises. Write these checks on an index card and keep it by
#   you while you complete the rest of these exercises or until you do not need the index card anymore:
# 1 Did you start your function definition with def?
# 2 Does your function name have only characters and _ (underscore) characters?
# 3 Did you put an open parenthesis ( right after the function name?
# 4 Did you put your arguments after the parenthesis ( separated by commas?
# 5 Did you make each argument unique (meaning no duplicated names)?
# 6 Did you put a close parenthesis and a colon ): after the arguments?
# 7 Did you indent all lines of code you want in the function four spaces? No more, no less.
# 8 Did you "end" function by going back to writing with no indent (dedenting)?

# When you run ("use" or "call") a function, check these things:
# 1 Did you call/use/run this function by typing its name?
# 2 Did you put the ( character after the name to run it?
# 3 Did you put the values you want into the parenthesis separted by commas?
# 4 Did you end the function call with a ) character?

# Use these two checklists on the remaining lessons until you do not need them anymore.

# Finally, repeat this a few times to yourself.
#       "To 'run,' 'call,' or 'use' a function all mean the same thing."
