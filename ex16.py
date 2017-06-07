# Exercise 16: Reading and Writing Files
# 06/01/2017

# If you did the Study Drills from the last exercise you should have seen all sorts of commands
# Methods/Functions you can give to files. Here's the list of commands you should remember.

# - close() -- Closes the file. Like File->Save.. in your editor
# - read() -- Reads the contents of the file. You can assign the result to a variable.
# - readline() -- Reads just one line of a text file.
# - truncate() -- Empties the file. Watch out if you care about the file.
# - write('stuff') -- Writes "stuff" to the file.

# For now these are the important commands you need to know. Some of them take parameters,
# but we do not really care about that. You only need to remember that write takes a parameters
# of a string you want to write to the file.

# Let's use some of this to make a simple little text editor:

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("? ")

print "Opening the file..."
target = open(filename, 'w') # Opening the file for writing.

print "Truncating the file. Goodbye!"
target.truncate() # Truncates the file's size. If the optional size arugment is present, the file is truncated to (at most) that size.
# Size defaults to the current position. Method does not work in case file is opened in read-only mode.
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") # Three separate lines of input in a newly created file.
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
formatter = "%s\n%s\n%s\n"
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(formatter % (line1, line2, line3))
print "And finally, we close it."
target.close()

# That's a large file, probably the largest you have typed in. So go slow, do your checks and make it run.
# One trick is to get bits of it running at a time.

# Study Drills
# 1 If you do not understand this, go back through and use the comment trick to get it squared away in your mind.
#       One simple english comment above each line will help you understand or a least let you know what you need to research more.
# 2 Write a script similar to the last exercise that uses read and argv to read the file you just created.
# 3 There's too much repetition in this file, use strings, formats and escapes to print out line1, line2 and line 3 with just
#       one target.write() command instead of six.
# 4 Find out why we had to pass a 'w' as an extra parameter to open. Hint: Open tries to be safe by making you explicitly say you
#       you want to write a file.
# 5 If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation for Python's open
#       function and see if that's true.

# Common Student Questions
# What does "w" mean?
#   It's really just a string with a chracter in it for the kind of mode for the file. If you use "w" then you're opening this file for writing.
#   "a" for append "r" for read.
# Does just doing open(filename) open it in "r" (read) mode?
#   Yes, that's the default for the open() function. 
