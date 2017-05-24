K#Exercise 3: Numbers and Math
print "I will now count my chickens: "
# Goes by precedence - left to right.
print "Hens", 25 + 30 / 6
# Multiplication over modulus
print "Roosters", 100 - 25 * 3 % 3

print "Now I will count the eggs: "
# (1/4) evaluates to 0 since it equals 0.25 due to truncation, 4 % 2 = 0
# Ends up evaluating to 6 - 5 + 6 from left to right. (PEMDAS)
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# The rest of the program deals with inequalities.
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
