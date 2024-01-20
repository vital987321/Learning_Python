from settings import *

player_record = ['Stepan', 'Normal', '6']
# player_record=['Nick', 'Hard', '6']
with open('scores.txt', 'r') as file:
    lines = file.readlines()
del lines[0]
records = [line.split() for line in lines]
print(records)
record_exists = False
for i in range(len(records)):
    if player_record[0] == records[i][0]:
        record_exists = True
        if player_record[2] > records[i][2]:
            records[i] = player_record
        break
if not record_exists:
    records.append(player_record)
print(records)
records = sorted(records, key=lambda x: int(x[2]), reverse=True)
print(records)
records = records[:MAX_RECORDS_NUMBER]
print(records)
with open('scores.txt', 'w') as file:
    file.write('Name\tLevel\tScore\n')
    for record in records:
        file.write(f'{record[0]}\t{record[1]}\t{record[2]}\n')
