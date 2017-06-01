# Exercise 13: Parameters, Unpacking, Variables
# 6/1/2016

# In this exercise we will cover one more input method you can use to pass variables to a script
# you know how you type "python ex13.py" to run the "ex13.py" file?
# well the ex13py part of the command is called an "argument"
# we'll learn how to write a script that also accepts arguments

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# on line 9 we have what's called an "import" this is how you add features to your script from the python feature set.
# Rather than give you all the features at once, python asks you what you plan to use.
# this keeps your programs small but also acts as documenttation for other programmers that read your code later.

# "argv" is the argument variable, standard name in programming and used in other languages,
# line 11 unpacks "argv" so that rather than holding all the arguments it gets assigned to four variables you can work with: script, first, second, and third.

# "Features" that can be imported are really called modules.
# these features will be later be referred as "import" modules. "You want to import the sys module" they are also called libraries but that's synonymous with modules.

# YOU MUST RUN THE PROGRAM LIKE THIS
# python ex13.py first 2nd 3rd
# The script is called: ex13.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd
