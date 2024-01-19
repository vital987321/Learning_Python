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
    except KeyboardInterrupt:
        print('Exit game')
    finally:
        get_status(player)
        print('Good buy!')

def get_status(player):
    print(f'\nPlayer: {player.name}.\tLives: {player.lives}.\tScore: {player.score}')

if __name__ == "__main__":
    play()

