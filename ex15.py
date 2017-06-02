# Exercise 15: Reading Files
# 06/01/2017

# You know how to get input from a user with raw_input or argv. now you will elarn about reading from a file.
# You may have to play with this exercise the most to understand what's going on, so do the exercise carefully
# and remember your checks.
# This exercise involves writing two files. One is the usual ex15.py file that you will run, but the other is named ex15_sample.txt
# This second file isnt a script but a plain text file we'll be reading in our script.

# ex15_sample.txt content:
#   This is stuff I typed into a file.
#   It is really cool stuff.
#   Lots and lots of fun to have in here.

# What we want to do is "open" that file in our script ad print it out.
# We don't want to hardcode the name ex15_sample.txt into our script.

from sys import argv # Importing sys library/module

script, file_name = argv # Stores script name as script and 1st argument as file_name
prompt = "> "
txt = open(file_name) # We open that file_name afterwards

print "Here's your file %r" % file_name
print txt.read() # Unlike C, we don't need to worry about end of files, Python just reads through the whole thing.
txt.close()
print "Type the file_name again: (ex15_sample.txt)"
file_again = raw_input(prompt) # Ask user to input the name of the same file.

txt_again = open(file_again) # Open the file once again, in order to read from it.

print txt_again.read() # Prints out all of the text within the file.
txt_again.close()
# Lines 18 - 19 use argv to get a file name. Next we have line 5 where we use a new command, open.
# pydoc open and read the instructions.
# Line 24 prints a little message - but on line

# Study Drills
# 1 Above each line, write out in english what the line does.
# 2 If you are not sure ask someone for help or search online. Many times searching for "python THING"
#       will find answers to what that THING does in python. Try searching for "python open"
# 3 I used the word "commands" here, but commands are also called "functions" and "methods"
#       You will learn about functions and methods later in the book.
# 4 Get rid of lines 27 - 32 where you use raw_input and run the script again.
# 5 Use only raw_input and try the script that way. Why is one way of getting the file name better than the other?
# 6 Start Python to start the python shell and use open from the prompt just like in this program.
# 7 Have your script also call close() on the txt and txt_again variables. It's Important to close files when you are done with them.
