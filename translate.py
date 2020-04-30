# translate.py uses the probabilistic dictionary from train.py to translate a
# given input.

import sys

# Read the dictionary into a Python dict where each word has its most probable
# translation

freq = {}

fd = open('spa-eng.tsv', 'r')

# For each word in the input, look up the word in the dict

# For each line in the spa-eng.tsv file...
for line in fd.readlines():

        # Strip newlines and split on the spaces...
        form = line.strip('\n').split(' ')

        # This prints out the form variable, which looks like [0.0, guarani, spoken]
        # print(form)

        # Add the translation to the lookup table

        # Is the source wordform not yet found in the translation table?
        if form[1] not in freq:
                freq[form[1]] = (form[0], form[2])

        # Is the probability of the translation higher than the existing one?
        if form[1] in freq and form[0] > freq[form[1]][0]:
                freq[form[1]] = (form[0], form[2])

# If the word has a translation, use it; otherwise output the input word with
# an asterisk *

text = sys.stdin.read()

words = text.strip('\n').split(' ')

# print(words)                  # words is a list, so this prints out the list

for word in words:
        # If the word has a translation, I want to print that translation
        if word in freq:
                print(freq[word][1], end=' ')
        # Otherwise, just print that word with an asterisk
        else:
                print('*' + word + ' ', end='')
