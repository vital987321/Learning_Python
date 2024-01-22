from game_exceptions import GameOver
from game_exceptions import EnemyDown
from game_exceptions import KeyboardInterrupt
from models import Player
from models import Enemy
from settings import *


def play():
    name = input("Enter your name: ")
    while True:
        try:
            level = LEVELS[input('Select level:\t 1-Normal.\t2-Hard: ')]
            break
        except KeyError:
            print('Incorrect input.')
    player = Player(name, level=level)
    enemy = Enemy(level)
    try:
        while True:
            get_status(player, enemy)
            try:
                player.attack(enemy)
            except EnemyDown:
                del enemy
                print("Congratulation! Enemy down.")
                player.score += POINTS_FOR_KILLING if level=='Normal' else POINTS_FOR_KILLING*HARD_MODE_MULTIPLIER
                enemy = Enemy(level)
                print("\nNew enemy comes.")
    except GameOver:
        print('You lost!')

    finally:
        get_status(player,enemy)

def get_status(player, enemy):
    print(f"\nPlayer: {player.name}."
          f"\tLevel: {player.level}."
          f"\tLives: {player.lives}."
          f"\tScore: {player.score}."
          f"\tEnemy's lives: {enemy.lives}")


def main_menu():
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
