# Exercise 24: More Practice
# 06/11/17

# This exercise is longer and all about building up stamina. The next exercise will be similar.
# Do them, get them exactly right, and do your checks.

print "Let's practice everything."
print 'You\'d need to know \'bout esapes with \\ that do \nnewlines and \ttabs.'
# Block text
poem = """
\tThe lovely world
with logic so firmly planted
canot discern\nthe needs of love
nor comprehend passion from institution
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 -6
print "This should be five: %s" % five
# Simple function/method
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars/100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
# Early variable concatenation
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10
# Instead of writing each separate variable like in line 36, we concatenate immediately.
print "We can also do that this way."
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
