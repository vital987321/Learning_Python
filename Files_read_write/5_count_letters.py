# task 5
# read zen_of_python.txt
# Count numbher of rows, words and letters.
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
ml = reduce(lambda x, y: alphabet_count[x] if alphabet_count[x]>alphabet_count[y] else alphabet_count[x] , alphabet_count)
# ml=reduce(lambda x, y:x if int(x.values())>int(y.values()) else y,alphabet_count)
print(ml)