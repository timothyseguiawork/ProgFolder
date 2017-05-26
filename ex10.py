# Exercise 10: What Was That?
# 05/26/17

tabby_cat = "\tI'm tabbed in." # Tab escape character
persian_cat = "I'm split\non a line." # Newline escape character
backslash_cat = "I'm \\ a \\ cat" # What kind of escape character is this?

# Prints a list using both newline and tab escape characters.
fat_cat = """
I'll do a list:
\t* Car food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# So this is an infinite loop that prints out all of the characters within the for statement.
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,
