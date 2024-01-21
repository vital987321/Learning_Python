from settings import *


class GameOver(Exception):
    def __init__(self, name: str, level: str, score: int):
        player_record = [name, level, score]
        with open('scores.txt', 'r') as file:
            lines = file.readlines()
        del lines[0]
        records = [line.split() for line in lines]
        record_exists = False
        for i in range(len(records)):
            if player_record[0] == records[i][0]:
                record_exists = True
                if player_record[2] > records[i][2]:
                    records[i] = player_record
                break
        if not record_exists:
            records.append(player_record)
        records = sorted(records, key=lambda x: int(x[2]), reverse=True)
        records = records[:MAX_RECORDS_NUMBER]
        with open('scores.txt', 'w') as file:
            file.write('Name\tLevel\tScore\n')
            for record in records:
                file.write(f'{record[0]}\t{record[1]}\t{record[2]}\n')


class EnemyDown(Exception):
    pass


class KeyboardInterrupt(Exception):
    def __init__(self):
        print('Exit game')


class IncorrectUserAttackInput(Exception):
    error_message = 'Incorrect input! User choice must be a number 1 ,2 or 3'


class FightError(Exception):
    pass
