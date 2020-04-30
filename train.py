# train.py file - takes 2 files of aligned sentences and produces a probabilistic
# dictionary.

import sys
import re

# Initialize the matrix
matrix = {}

vocab1 = list(set(open('spa.txt', 'r').read().split()))
vocab2 = list(set(open('eng.txt', 'r').read().split()))

# Add each combination of words to a matrix (dictionary of dictionaries) where the
# keys are the words and the final value is the count
# This will initialize the matrix
for w1 in vocab1:
        if w1 not in matrix:
                matrix[w1] = {}
        for w2 in vocab2:
                if w2 not in matrix[w1]:
                        matrix[w1][w2] = 0

# Open the 2 input files
file1 = open('spa.txt', 'r')
file2 = open('eng.txt', 'r')

# In a while loop, read one line from each file
line1 = file1.readline()
line2 = file2.readline()

re.sub(r'([.,])', r' \1', line1)
re.sub(r'([.,])', r' \1', line2)

# This while loop collects the counts
while True:
        # Test to see if we have reached the end of the file
        if line1.strip() == '' or line2.strip() == '':
                break

        # Read one line from each file
        line1 = file1.readline()
        line2 = file2.readline()

        re.sub(r'([.,])', r' \1', line1)
        re.sub(r'([.,])', r' \1', line2)
       
        # Split the lines into words
        tokens1 = line1.split()
        tokens2 = line2.split()

        # Create the matrix of cooccurrence counts
        for token1 in tokens1:
                for token2 in tokens2:
                        matrix[token1][token2] += 1

# Iterate through the matrix and print out the value of each word pair combination
# divided by the total for that word

# print(matrix)

for w1 in matrix:
        total = 0
        for w2 in matrix[w1]:
                total += matrix[w1][w2]
        if total == 0:
                continue
        for w2 in matrix[w1]:
                print(matrix[w1][w2]/total, w1, w2)
