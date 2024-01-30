""" This file is the entry file. Run it to start."""

from game_exceptions import GameOver, \
    EnemyDown, \
    QuitApp, \
    WhiteSpaceInputError, \
    EmptyInputError
from models import Player, Enemy
from settings import MODES, \
    MODE_NORMAL, \
    MODE_HARD, \
    MAX_RECORDS_NUMBER, \
    SCORE_FILE, \
    ALLOWED_ATTACKS
from functools import reduce

__version__ = '1'


def is_valid_name(name: str) -> bool:
    """Validates user input name"""

    if ' ' in name:
        raise WhiteSpaceInputError
    elif not name:
        raise EmptyInputError
    return True


def input_name() -> str:
    """Input and return player name."""
    while True:
        name = input("Enter your name: ")
        try:
            if is_valid_name(name):
                return name
        except WhiteSpaceInputError:
            print("Whitespaces are not allowed in the name.")
        except EmptyInputError:
            print('Name cannot be empty.')


def get_allowed_options(options_dict: dict) -> tuple:
    return tuple(options_dict.keys())


def is_valid_input_mode(mode_input: str) -> bool:
    """Validates mode input"""
    return mode_input in get_allowed_options(MODES)


def input_mode() -> str:
    """Input and return game mode"""
    while True:
        mode_input = input(f'Select game mode:\t 1-{MODE_NORMAL}.\t2-{MODE_HARD}: ')
        if is_valid_input_mode(mode_input):
            return MODES[mode_input]
        print('Incorrect input.')


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
                level += 1
                enemy = Enemy(mode, level)  # new enemy replaces the previous one.
                print("\nNew enemy comes.")

    except GameOver:
        print('You lost!')
        save_score(player)

    finally:
        print_status(player, enemy)


def read_records() -> list[list[str]]:
    """read records from board file to list"""
    with open(SCORE_FILE, 'r') as file:
        lines = file.readlines()
    del lines[0]
    return [line.split() for line in lines]


def add_record_to_list(player_record: list, records: list[list[str]]) -> list[list[str]]:
    """add current result to list"""
    record_exists = False
    for i in range(len(records)):
        if player_record[0] == records[i][0]:
            record_exists = True
            if player_record[2] > int(records[i][2]):
                records[i] = player_record
            break
    if not record_exists:
        records.append(player_record)
    return records


def sort_records(records: list[list[str]]) -> list[list[str]]:
    """Sorts records based on score in reversed order"""
    return sorted(records, key=lambda x: int(x[2]), reverse=True)


def save_to_file(records: list[list[str]]) -> None:
    """save scores to file"""
    name_column_size = reduce(lambda x, y: max(x, len(y[0])), records, 0) + 4
    with open(SCORE_FILE, 'w') as file:
        file.write(f'{"NAME".ljust(name_column_size)}{"MODE".ljust(10)}SCORE\n')
        for record in records:
            file.write(f'{record[0].ljust(name_column_size)}{record[1].ljust(10)}{record[2]}\n')


def save_score(player: Player) -> None:
    """ Saves score to board file"""
    player_record = [player.name, player.mode, player.score]
    records = read_records()
    records = add_record_to_list(player_record, records)
    records = sort_records(records)
    records = records[:MAX_RECORDS_NUMBER]
    save_to_file(records)


def print_status(player: Player, enemy: Enemy) -> None:
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
    return menu_input in get_allowed_options(ALLOWED_ATTACKS)


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
        print('Incorrect input.')


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
