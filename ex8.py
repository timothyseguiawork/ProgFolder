# Exercise 8: Printing, Printing
# 05/26/17

# Using a format as a variable to style specific variables you want at compile time.
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) # 1 2 3 4
print formatter % ("one", "two", "three", "four") # one two three four
print formatter % (True, False, False, True) # True False False True
print formatter % (formatter, formatter, formatter, formatter) # Prints out
# '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
print formatter % (
    "I had this thing.",
    "That you could type it up right.",
    "But it didn't sing",
    "So I said goodnight."
    ) # Prints out exact text with spaces inbetween.
