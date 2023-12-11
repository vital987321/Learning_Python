# task 3.
# In input file 3_input.txt there are a list of integers separated by a spacer or by new line.
# Write application that calculates the sum of all the integers and writes the result to 3_output.txt.

with open('3_input.txt') as input_file:
    text = input_file.read()
numbers = text.split()
result = 0
for number in numbers:
    try:
        result += int(number)
    except:
        print(f'Value "{number}" is not a number. Value is ignored.')
with open('3_output.txt', 'w') as output:
    output.write(str(result))
