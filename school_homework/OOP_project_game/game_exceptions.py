from settings import *
from functools import reduce


class GameOver(Exception):
    def __init__(self, name: str, level: str, score: int):
        player_record = [name, level, score]
        with open(SCORE_FILE, 'r') as file:
            lines = file.readlines()
        del lines[0]
        records = [line.split() for line in lines]
        record_exists = False
        for i in range(len(records)):
            if player_record[0] == records[i][0]:
                record_exists = True
                if player_record[2] > int(records[i][2]):
                    records[i] = player_record
                break
        if not record_exists:
            records.append(player_record)
        records = sorted(records, key=lambda x: int(x[2]), reverse=True)
        records = records[:MAX_RECORDS_NUMBER]
        name_column_size=reduce(lambda x,y:max(x,len(y[0])),records,0)+4
        with open(SCORE_FILE, 'w') as file:
            file.write(f'{"NAME".ljust(name_column_size)}{"LEVEL".ljust(10)}SCORE\n')
            for record in records:
                file.write(f'{record[0].ljust(name_column_size)}{record[1].ljust(10)}{record[2]}\n')


class EnemyDown(Exception):
    pass


class KeyboardInterrupt(Exception):
    def __init__(self):
        print('Exit game')


class FightError(Exception):
    pass
