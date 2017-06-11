# Exercise 25: Even More Practice
# 06/11/17

# This exercise is a little different, you're going to import it into python and
# run the functions yourself.

# This tokenizies the string you first create.
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
# This then sorts the words based in that string after breaking the words up.
def sort_words(words):
    """Sorts the words"""
    return sorted(words)
# Goes into the stack of words and takes out the first word within the stack.
# Removes the first word from the stack and changes the "words" variable entirely.
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
# Removes the last word from within the stack, and changes the words variable entirely.
def print_last_word(words):
    """Prints the last wrod after popping it off."""
    word = words.pop(-1)
    print word
# Sorts the original sentence one creates.
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
# Takes both the first and last word from a sentence.
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
# Takes both the first and last word from a sorted sentence.
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Type 'python' into the console after checking whether or not the file is correct.
# Python 2.7.11 (default, Jan 22 2016, 23:30:40)
# [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25 # importing the script
# >>> sentence = "All good things come to those who wait." # creating your sentence
# >>> words = ex25.break_words(sentence) # breaking up those words to create a stack of words
# >>> words # print out your variable
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words) # sorting the stack of words
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words) # pops the forst word and prints it.
# All
# >>> ex25.print_last_word(words) # pops the last word and prints it.
# wait.
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who'] # notice that 'all' and 'wait.' aren't in the stack anymore?
# >>> ex25.print_first_word(sorted_words) # printing the first word of a sorted break_words
# All
# >>> ex25.print_last_word(sorted_words)  # printing the last word of a sorted break_words
# who
# >>> sorted_words # notice that "ALL" and "who" aren't in the stack anymore.
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence) # we recreate our sentence because our two original words are missing.
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who'] # "All" and "who" are back!
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
