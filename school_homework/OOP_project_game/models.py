""" module contains Enemy Class and Player Class"""

from game_exceptions import *
from settings import *
from random import randint


class Enemy():
    """Class represents the enemy bot player"""
    lives: int

    def __init__(self, level: str):
        self.lives = ENEMY_LIVES if level == 'Normal' else ENEMY_LIVES * HARD_MODE_MULTIPLIER

    def attack(self) -> str:
        """randomly returns one of possible enemy's attack"""
        return ALLOWED_ATTACKS[str(randint(1, 3))]

    def decrease_lives(self):
        '''Decrease enemy's lives'''
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()


class Player():
    """Class describes user's player"""
    name: str
    score: int
    level: str

    def __init__(self, name: str, level: str):
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0
        self.level = level

    def attack(self, enemy: Enemy) -> None:
        """
        Asks the user to choose the attack.
        Then calls the fight method.
        Based on the fight result calls corresponding method.
        """

        # select player attack
        while True:
            try:
                player_attack = ALLOWED_ATTACKS[input('Select attack:\n'
                                                      '\t1 - Paper\n'
                                                      '\t2 - Stone\n'
                                                      '\t3 - Scissors\n'
                                                      '\t(0 - Exit Game)\n'
                                                      '\t: ')]
                if player_attack == 'Exit Game':
                    raise KeyboardInterrupt()
                break
            except KeyError:
                print('Incorrect input.')

        # resolve fight
        fight_result = self.__fight(player_attack, enemy)
        if fight_result == 1:
            print('You attacked successfully!')
            self.__on_win_fight(enemy)
        elif fight_result == -1:
            print("You missed!")
            self.decrease_lives()
        elif fight_result == 0:
            print("It's a draw!")
        else:
            raise FightError

    def __fight(self, player_attack: str, enemy: Enemy) -> int:
        """Resolves player's attack vs enemy's attack"""
        enemy_attack = enemy.attack()
        print(f"Your attack: {player_attack}.  Enemy's attack: {enemy_attack}")
        if player_attack == enemy_attack:
            return 0
        elif player_attack == 'Paper' and enemy_attack == 'Stone':
            return 1
        elif player_attack == 'Paper' and enemy_attack == 'Scissors':
            return -1
        elif player_attack == 'Stone' and enemy_attack == 'Paper':
            return -1
        elif player_attack == 'Stone' and enemy_attack == 'Scissors':
            return 1
        elif player_attack == 'Scissors' and enemy_attack == 'Paper':
            return 1
        elif player_attack == 'Scissors' and enemy_attack == 'Stone':
            return -1
        else:
            raise FightError

    def decrease_lives(self) -> None:
        """Decreases player's lives"""
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self.name, self.level, self.score)

    def __on_win_fight(self, enemy: Enemy) -> None:
        """Adds score in case successful fight"""
        self.score += POINTS_FOR_FIGHT if self.level == 'Normal' else POINTS_FOR_FIGHT * HARD_MODE_MULTIPLIER
        enemy.decrease_lives()
