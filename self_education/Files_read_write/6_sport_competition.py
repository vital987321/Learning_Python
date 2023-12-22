# Task 6
# File 6_first_tour.txt contains a number K and a list of sportsmen
# with their score after first round. Format is the following:
#   80
#   Zuckerberg Mark 80
#   Musk Ilon 92
#   Gates Bill 98
#   Jobs Steve 78
#
# Filter the list of sportsmen for the second round. Criteria is a score must be greater than K.
# Write result to file 6_second_tour.txt in the following format:
#   2
#   1)	B. Gates 98
#   2)	I. Musk 92
# The first number shows the number of participants.


with open('6_first_tour.txt') as readfile:
    passrate = int(readfile.readline())
    first_round_list = readfile.read().splitlines()
for i in range(len(first_round_list)):
    first_round_list[i] = first_round_list[i].split()
print(first_round_list)
second_round_list = list(filter(lambda x: int(x[2]) > passrate, first_round_list))
print(second_round_list)
result = f'{len(second_round_list)}\n'
i = 0
for man in second_round_list:
    i += 1
    result += f'{i}) {man[1][0]}. {man[0]} {man[2]}\n'
print(result)
with open('6_second_tour.txt', 'w') as writefile:
    writefile.write(result)
