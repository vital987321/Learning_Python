""" This file is the entry file. Ran it to start."""

from game_exceptions import GameOver, EnemyDown, KeyboardInterrupt
from models import Player, Enemy
from settings import ALLOWED_ATTACKS, \
    MODES, \
    PLAYER_LIVES, \
    ENEMY_LIVES, \
    POINTS_FOR_FIGHT, \
    POINTS_FOR_KILLING, \
    MAX_RECORDS_NUMBER, \
    HARD_MODE_MULTIPLIER, \
    SCORE_FILE

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
    if mode_input in ['1', '2']:
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
    enemy = Enemy(mode)

    # main fight
    try:
        while True:
            get_status(player, enemy)
            try:
                player.attack(enemy)
            except EnemyDown:
                del enemy
                print("Congratulation! Enemy down.")
                player.add_score()
                enemy = Enemy(mode)
                print("\nNew enemy comes.")

    except GameOver:
        print('You lost!')

    finally:
        get_status(player, enemy)


def get_status(player, enemy) -> None:
    '''Prints the current game status to console'''
    print(f"\nPlayer: {player.name}."
          f"\tMode: {player.mode}."
          f"\tLives: {player.lives}."
          f"\tScore: {player.score}."
          f"\tEnemy's lives: {enemy.lives}")


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
            with open(SCORE_FILE) as file:
                print(file.read())
        elif choice == '3':
            raise KeyboardInterrupt()
        else:
            print('Incorrect command!')


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print('Good buy!')
