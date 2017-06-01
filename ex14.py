# Exercise 14: Prompting and Passing
# 06/01/2017

# Lets do one exercise that uses argv and raw_input together to ask the user something specific. You will need this for the next exercise
# When we learn to read and write files. In this exercise we'll use raw_input slightly differently by having it print a simple > prompt
# Similar to a game like Zork or adventure

from sys import argv


script, user_name, lastName = argv # python ex14.py user_name (original), python ex13.py user_name lastName (study drill)
prompt ='$ '#(study drill 2) #'> ' #(original)

print "Hi %s %s, I'm the %s script." % (user_name, lastName, script) # Takes argument varaibles, name input by user and the script name
print "I'd like to ask you a few questions."
print "Do you like me? %s %s? y/n" % (user_name, lastName)
likes = raw_input(prompt) # Accepts raw input for the questions, What's very interesting is that it waits for your answer

print "Where do you live %s %s?" % (user_name, lastName)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
Your name is %s %s.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, user_name, lastName, lives, computer) # line 27 added for study drill 3

# We make a variable prompt that is set to the prompt we want, and we give that to raw_input instead of typing it over and over.
# If we want to change it to something else, we just change it in that one spot on line 12 and rerun the script.

# Study Drills
# 1 Figure out what Zork and Adventure were. Try to find a copy and play it (already played it)
# 2 Change the prompt to something entirely and see how it works
#       Changing prompt to "$"
# 3 Add another argument and use it in your script, the same way you did in the previous exercise with first, second = argv
# 4 Make sure you understand how one combines a block quote with % format activator as the last print
