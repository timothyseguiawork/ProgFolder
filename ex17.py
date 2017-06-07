# Exercise 17: More Files
# 06/06/17

# Now lets do a few more things with files. We'll write a Python Script to copy one file to another.
# It'll be very short ut will give you ideas about other things you can do with files.

from sys import argv # Similar to accepting a list of the arguments to your program
from os.path import exists # Implements some useful functions on pathnames.
# python ex16.py file1 file2 (execution command)
script, from_file, to_file = argv # script = ex16.py, from_file = file1, to_file = file2 (Original code)
# Prints copying from file1, file2 fi following example above.
# print "Copying from %s to %s" % (from_file, to_file) # Original Code

# We could do these two on one line, how?
# in_file = open(from_file) # Original Code
# indata = in_file.read() # Original Code

# print "The input file is %d bytes long" % len(indata) # Original Code
# exists command imported. Returns true if a file exists, based on its name in a string as an argument.
# print "Does the output file exist? %r" % exists(to_file) # exists returns false if not. # Original Code
# print "Ready, hit RETURN to continue, CTRL-C to abort." # Original Code
# raw_input("> ") # Original Code

with open(to_file, 'w') as f: # Result of study drill 2
    f.write(open(from_file,'r').read())

# out_file = open(to_file, 'w') # Original Code
# print "Writing data..." # Original Code
# out_file.write(indata) # Original Code

# print "Alright, all done." # Original Code

# out_file.close() # Original Code
# Don't really need closes at all, mainly because of automatic closing at garbage collection
# in_file.close() # Original Code

# Study Drills:
# 1 This script is really annoying. There's no need to ask you before doing the copy and it prints too much
#       to the screen. Try to make the script more friendly to use by removing features.
# 2 See how short you could make the script, I could make this one line long.
# 3 Notice at the end of the "WHAT YOU SHOULD SEE" I used something called cat?
#       It's an old command that can "con*cat*enate" files together, but mostly it's just an easy way to print
#       a file to the screen. Type "man cat" to read about it.
# 4 Find out why you had to write out_file.close() in the code.
# 5 Go read up on Python's import statement, and start python to try it out. Try importing some things and
#       see if you can get it right. It's alright if you don't.
