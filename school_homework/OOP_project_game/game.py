from game_exceptions import GameOver
from game_exceptions import EnemyDown
from game_exceptions import KeyboardInterrupt
from models import Player
from models import Enemy


def play():
    name = input("Enter your name: ")
    user = Player(name)
    enemy = Enemy()


if __name__ == "__main__":
    try:
        play()
    except GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Good buy!')
