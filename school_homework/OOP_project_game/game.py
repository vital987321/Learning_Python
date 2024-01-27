""" This file is the entry file. Ran it to start."""

from game_exceptions import GameOver, EnemyDown, QuitApp
from models import Player, Enemy
from settings import ALLOWED_ATTACKS, \
    MODES, \
    PLAYER_LIVES, \
    POINTS_FOR_FIGHT, \
    POINTS_FOR_KILLING, \
    MAX_RECORDS_NUMBER, \
    HARD_MODE_MULTIPLIER, \
    SCORE_FILE
from functools import reduce

__version__ = '1'


def is_valid_name(name: str) -> bool:
    """Validates user input name"""

    if ' ' in name:
        print("Whitespaces are not allowed in the name.")
        return False
    elif not name:
        print('Name cannot be empty.')
        return False
    return True


def input_name() -> str:
    while True:
        name = input("Enter your name: ")
        if is_valid_name(name):
            return name


def is_valid_input_mode(mode_input: str) -> bool:
    if mode_input in ('1', '2'):
        return True
    return False


def input_mode() -> str:
    while True:
        mode_input = input('Select game mode:\t 1-Normal.\t2-Hard: ')
        if is_valid_input_mode(mode_input):
            return MODES[mode_input]


def play() -> None:
    """Runs the main game"""

    # input name
    name = input_name()

    # input game mode
    mode = input_mode()

    # make players
    player = Player(name, mode=mode)
    level=1
    enemy = Enemy(mode, level)

    # main fight
    try:
        while True:
            print_status(player, enemy)
            try:
                player.attack(enemy)
            except EnemyDown:
                player.on_enemy_down()
                del enemy
                level+=1
                enemy = Enemy(mode, level)
                print("\nNew enemy comes.")

    except GameOver:
        print('You lost!')
        save_score(player)

    finally:
        print_status(player, enemy)

def save_score(player:Player)->None:
    player_record = [player.name, player.mode, player.score]

    # reads records from file to list
    with open(SCORE_FILE, 'r') as file:
        lines = file.readlines()
    del lines[0]
    records = [line.split() for line in lines]

    # add current result to list
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

    # save list to file
    name_column_size = reduce(lambda x, y: max(x, len(y[0])), records, 0) + 4
    with open(SCORE_FILE, 'w') as file:
        file.write(f'{"NAME".ljust(name_column_size)}{"MODE".ljust(10)}SCORE\n')
        for record in records:
            file.write(f'{record[0].ljust(name_column_size)}{record[1].ljust(10)}{record[2]}\n')

def print_status(player, enemy) -> None:
    """Prints the current game status to console"""
    print(f"\nPlayer: {player.name}."
          f"\tMode: {player.mode}."
          f"\tPlayer Lives: {player.lives}."
          f"\tScore: {player.score}."
          f"\tLevel: {enemy.level}"
          f"\tEnemy's lives: {enemy.lives}")

def print_score()->None:
    """Reads score from file and print it"""
    with open(SCORE_FILE) as file:
        print(file.read())

def main_menu() -> None:
    """Displays the main menu of the game"""
    while True:
        print("\n----Main Menu----")
        choice = input('Select command:\n'
                       '\t1-Start new game\n'
                       '\t2-Show scores\n'
                       '\t3-Exit game\n'
                       '\t: ')
        if choice == '1':
            play()
        elif choice == '2':
            print_score()
        elif choice == '3':
            raise QuitApp
        else:
            print('Incorrect command!')


if __name__ == "__main__":
    try:
        main_menu()
    except QuitApp:
        print('Good buy!')
    except KeyboardInterrupt:
        print('Good buy!')
