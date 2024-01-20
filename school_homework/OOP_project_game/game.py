from game_exceptions import GameOver
from game_exceptions import EnemyDown
from game_exceptions import KeyboardInterrupt
from models import Player
from models import Enemy
from settings import *


def play():
    name = input("Enter your name: ")
    level=input('Select level:\t 1-Normal.\t2-Hard: ')      # need validation
    player = Player(name, level=LEVELS[level])
    enemy = Enemy()
    try:
        while True:
            get_status(player)
            try:
                player.attack(enemy)
            except EnemyDown:
                del enemy
                print("Congratulation! Enemy down.")
                player.score += POINTS_FOR_KILLING
                enemy = Enemy()
                print("\nNew enemy comes.")
    except GameOver:
        print('You lost!')
        save_score(player)

    except KeyboardInterrupt:
        print('Exit game')
    finally:
        get_status(player)
        print('Good buy!')

def save_score(player:Player):
    player_record = [player.name, player.level, player.score]
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

def get_status(player):
    print(f'\nPlayer: {player.name}.\tLevel: {player.level}.\tLives: {player.lives}.\tScore: {player.score}')

def main_menu():
    print("\n----Main Menu----")
    choice=input('Select command:\n\t1-Start new game\n\t2-Show scores\n\t3-Exit game\n\t') # validation needed
    if choice=='1':
        play()
    elif choice=='2':
        with open('scores.txt') as file:
            print(file.read)
if __name__ == "__main__":
    main_menu()
    # play()

