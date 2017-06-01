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

from sys import argv

script, file_name = argv
prompt = "> "
txt = open(file_name)

print "Here's your file %r" % file_name
print txt.read() # Unlike C, we don't need to worry about end of files, Python just reads through the whole thing.

print "Type the file_name again:"
file_again = raw_input(prompt)

txt_again = open(file_again)

print txt_again.read()

# Lines 18 - 19 use argv to get a file name. Next we have line 5 where we use a new command, open.
# pydoc open and read the instructions.
# Line 24 prints a little message - but on line
