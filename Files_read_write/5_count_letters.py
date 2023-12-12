# task 5
# read zen_of_python.txt
# Count number of rows, words and letters.
# Find the lest used letter in the text.

import string
from functools import reduce
with open('zen_of_Python.txt') as file:
    lines = file.readlines()
rows_number=len(lines)
words='\n'.join(lines).split()
words_number=len(words)
symbols=''.join(words).lower()
letters_number=0
alphabet_count={letter:0 for letter in string.ascii_lowercase}

for symbol in symbols:
    if symbol.isalpha():
        letters_number+=1
        alphabet_count[symbol]+=1

least_used_letter = reduce(lambda x, y: x if alphabet_count[x]<alphabet_count[y] else y , alphabet_count,'a')

print(f'Number of rows: {rows_number}')
print(f'Number of words: {words_number}')
print(f'Number of letters: {letters_number}')
print(f'The least used letter is "{least_used_letter}". It is used {alphabet_count[least_used_letter]} times.')