# Exercise 20: Functions and Files
# 06/07/2017

# Remember your checklist for functions, then do this exercise paying close
#   attention to how functions and files can work together to make useful stuff.

from sys import argv

script, input_file = argv
# Prints all of the contents of input_file
def print_all(f):
    print f.read()
# Resets offset/seek to 0, beginning of the file.
def rewind(f):
    f.seek(0)
# Prints a line based on seek. Seek goes by line rather than character?
def print_a_line(line_count, f):
    print line_count, f.readline()
# opening the file for reading, default option for open.
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines: "

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
