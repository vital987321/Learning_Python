# Task:
# There is hw.txt file with some text.
# Output all words from the file in reverse order and remove punctuations.

text = ''
try:
    file = open('hw1.txt')
    text = file.read()
    file.close()
except:
    print('file not found')

if text:
    text.strip()  # remove beginning/end spacers
    punctuation = '.,-*!?:;'
    text = ''.join(symbol for symbol in text if not symbol in punctuation)  # removing punctuations and line feeds
    text = ' '.join(word for word in text.split()[::-1])
    print(text)
