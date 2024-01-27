""" This file is the entry file. Run it to start."""

from game_exceptions import GameOver, EnemyDown, QuitApp
from models import Player, Enemy
from settings import MODES, \
    MODE_NORMAL, \
    MODE_HARD, \
    MAX_RECORDS_NUMBER, \
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
    """Input and return player name."""
    while True:
        name = input("Enter your name: ")
        if is_valid_name(name):
            return name


def is_valid_input_mode(mode_input: str) -> bool:
    """Validates mode input"""
    if mode_input in ('1', '2'):
        return True
    return False


def input_mode() -> str:
    """Input and return game mode"""
    while True:
        mode_input = input(f'Select game mode:\t 1-{MODE_NORMAL}.\t2-{MODE_HARD}: ')
        if is_valid_input_mode(mode_input):
            return MODES[mode_input]


def play() -> None:
    """Runs the main game"""
    # game level
    level = 1
    # input name
    name = input_name()
    # input game mode
    mode = input_mode()

    player = Player(name, mode=mode)
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
                level += 1
                enemy = Enemy(mode, level)
                print("\nNew enemy comes.")

    except GameOver:
        print('You lost!')
        save_score(player)

    finally:
        print_status(player, enemy)


def save_score(player: Player) -> None:
    """ Saves score to board file"""
    player_record = [player.name, player.mode, player.score]

    # read records from file to list
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


def print_score() -> None:
    """Reads score from file and prints it"""
    with open(SCORE_FILE) as file:
        print(file.read())


def is_valid_menu_input(menu_input: str) -> bool:
    """ Validates menu user input"""
    if menu_input in ('1', '2', '3'):
        return True
    print('Incorrect input.')
    return False


def main_menu_input() -> str:
    """Menu user input"""
    while True:
        print("\n----Main Menu----")
        menu_choice = input('Select command:\n'
                            '\t1-Start new game\n'
                            '\t2-Show scores\n'
                            '\t3-Exit game\n'
                            '\t: ')
        if is_valid_menu_input:
            return menu_choice


def main_menu() -> None:
    """Displays the main menu of the game"""
    menu_choice = main_menu_input()
    if menu_choice == '1':
        play()
    elif menu_choice == '2':
        print_score()
    elif menu_choice == '3':
        raise QuitApp


if __name__ == "__main__":
    """ App entry point"""
    try:
        main_menu()
    except QuitApp:
        print('Good buy!')
    except KeyboardInterrupt:
        print('Good buy!')
