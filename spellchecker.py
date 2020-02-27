"""
This spellchecker.py file will take a word and see if it exists in the list of words
from your frequency list. If the word exists, it will print out the word; if the word
does not exist, it will print out an asterix followed by the word.
"""

import sys

# (1) Load the frequency list from the file argument into a python list

# Dictionary to store frequency list (easier/faster lookup than a [] list)
freq = {}

# Open the freq.txt file, save it as variable fd
fd = open('freq.txt', 'r')

# (2) Read standard input line by line
for line in fd.readlines():
        # (3) Split each line into tokens - the form is the line without spacing
        form = line.strip('\n')
        # (4) For each of the tokens, see if it exists in the list/dictionary
        # If we haven't seen it yet, then set that token's frequency count to 0
        if form not in freq:
                freq[form] = 0
        # Otherwise, if we have seen it before, increase the frequency count by 1
        freq[form] = freq[form] + 1

# (5) If it exists, print it out; otherwise print it out with an asterix

# Read in the standard input, save it as variable text
text = sys.stdin.read()

# Split the text on the spaces, save this as a list named words
# NOTE: .split() creates a list
words = text.split(' ')

# Iterate through the words list
for word in words:
        # If the word exists in the freq dictionary, print it out
        if word in freq:
                print(word)
        # Otherwise, print out an asterix followed by the word
        # NOTE: end='' displays the output all on one line, rather than line by line
        else:
                print('*' + word + ' ', end='')

# INPUT: echo "There aren't enuf hours in teh day." | python3 spellchecker.py wiki.hist
# EXPECTED OUTPUT: There aren't *enuf hours in *teh day.
# ACTUAL OUTPUT: it will show every word with an asterix, because my freq.txt file is not in English.
# *There *aren't *enuf *hours *in *teh *day.
