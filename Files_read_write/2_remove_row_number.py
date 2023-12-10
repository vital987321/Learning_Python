# Task:
# There is hw.txt file with some text.
# User inputs a row number. Remove this row from the text and save the text to separate file.

with open('hw1.txt') as input_file:
    lines=input_file.readlines()
while True:
    try:
        user_row=int(input('Enter row number: '))
        break
    except:
        print('This is not a number.')

print(lines)
lines.pop(user_row-1)
print(lines)

with open('2_remove_row_number_result.txt', 'w') as output_file:
    for row in lines:
        output_file.write(row)