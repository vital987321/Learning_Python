""" This file is the entry file. Run it to start."""

from game_exceptions import GameOver, EnemyDown, QuitApp, WhiteSpaceInputError, EmptyInputError, RecordInRecordsError
from models import Player, Enemy
from school_homework.OOP_project_game.record import GameRecord
from school_homework.OOP_project_game.validations import validate_name, is_valid_input_mode, is_valid_menu_input
from settings import MODES, MODE_NORMAL, MODE_HARD, SCORE_FILE

__version__ = '1'


class Game:
    _level = 1
    _name: str
    _mode: str
    player: Player
    enemy: Enemy

    def __init__(self):
        self.create_player()
        self.new_enemy()

    def input_name(self) -> None:
        """Input and return player name."""
        while True:
            name = input("Enter your name: ")
            try:
                validate_name(name)
                self._name = name
                break
            except WhiteSpaceInputError:
                print("Whitespaces are not allowed in the name.")
            except EmptyInputError:
                print('Name cannot be empty.')

    def input_mode(self) -> None:
        """Input and return game mode"""
        while True:
            mode_input = input(f'Select game mode:\t 1-{MODE_NORMAL}.\t2-{MODE_HARD}: ')
            if is_valid_input_mode(mode_input):
                self._mode = MODES[mode_input]
                break
            print('Incorrect input.')

    def create_player(self) -> None:
        self.input_name()
        self.input_mode()
        self.player = Player(name=self._name, mode=self._mode)

    def new_enemy(self) -> None:
        self.enemy = Enemy(mode=self._mode, level=self._level)

    def print_status(self) -> None:
        """Prints the current game status to console"""
        print(f"\nPlayer: {self.player.name}."
              f"\tMode: {self.player.mode}."
              f"\tPlayer Lives: {self.player.lives}."
              f"\tScore: {self.player.score}."
              f"\tLevel: {self.enemy.level}"
              f"\tEnemy's lives: {self.enemy.lives}")

    def increase_level(self) -> None:
        self._level += 1

    def save_score(self) -> None:
        """ Saves score to board file"""
        game_record = GameRecord()
        try:
            game_record.add_record(self.player)
            game_record.save_to_file()
        except RecordInRecordsError:
            print('Record is already in list')

    def enemy_down(self) -> None:
        self.player.on_enemy_down()
        self.increase_level()
        self.new_enemy()
        print("\nNew enemy comes.")

    def start_game(self) -> None:
        try:
            while True:
                self.print_status()
                try:
                    self.player.attack(self.enemy)
                except EnemyDown:
                    self.enemy_down()
        except GameOver:
            print('You lost!')
            self.save_score()

        finally:
            self.print_status()


def play() -> None:
    """Runs the main game"""
    game = Game()
    game.start_game()


def print_score() -> None:
    """Reads score from file and prints it"""
    with open(SCORE_FILE) as file:
        print(file.read())


def main_menu_input() -> str:
    """Menu user input"""
    while True:
        print("\n----Main Menu----")
        menu_choice = input('Select command:\n'
                            '\t1-Start new game\n'
                            '\t2-Show scores\n'
                            '\t3-Exit game\n'
                            '\t: ')
        if is_valid_menu_input(menu_choice):
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


def main():
    try:
        main_menu()
    except QuitApp:
        print('Good buy!')
    except KeyboardInterrupt:
        print('Good buy!')
