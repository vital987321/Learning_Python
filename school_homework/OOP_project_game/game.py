from game_exceptions import GameOver
from game_exceptions import EnemyDown
from game_exceptions import KeyboardInterrupt
from models import Player
from models import Enemy
from settings import *


def play():
    name = input("Enter your name: ")
    player = Player(name)
    enemy = Enemy()
    try:
        player.attack(enemy)
    except EnemyDown:
        del enemy
        print("Congratulation! Enemy down.")
        player.score += POINTS_FOR_KILLING
        enemy = Enemy()
        print("\nNew enemy comes.")


if __name__ == "__main__":
    try:
        play()
    except GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Good buy!')
