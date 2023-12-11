# task 4
# There is a file 4_zen_of_python.txt with 19 statements of the philosophy of python.
# Output all statements in reversed order

# with open('4_Zen_of_python.txt') as input_file:
#     lines=input_file.readlines()
# for line in lines[::-1]:
#     print (line)

with open('4_Zen_of_python.txt') as input_file:
    text=input_file.read()
lines=text.split('\n')
for line in lines[::-1]:
    print (line)