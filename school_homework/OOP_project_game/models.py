""" module contains Enemy Class and Player Class"""

from game_exceptions import GameOver, \
    EnemyDown, \
    QuitApp
from settings import ALLOWED_ATTACKS, \
    MODE_NORMAL, \
    PLAYER_LIVES, \
    POINTS_FOR_FIGHT, \
    POINTS_FOR_KILLING, \
    HARD_MODE_MULTIPLIER, \
    ATTACK_PAIRS_OUTCOME
from random import randint


class Enemy():
    """Class represents the enemy bot player"""
    lives: int
    level: int

    def __init__(self, mode: str, level: int):
        self.level = level
        self.lives = self.level if mode == MODE_NORMAL else self.level * HARD_MODE_MULTIPLIER

    def attack(self) -> str:
        """randomly returns one of possible enemy's attack"""
        return ALLOWED_ATTACKS[str(randint(1, 3))]

    def decrease_lives(self) -> None:
        """Decrease enemy's lives"""
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player():
    """Class describes user's player"""
    name: str
    score: int
    mode: str

    def __init__(self, name: str, mode: str):
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0
        self.mode = mode

    @staticmethod
    def __is_valid_input_attack(attack_input: str) -> bool:
        """ Validates attack input"""
        from game import get_allowed_options
        return attack_input in get_allowed_options(ALLOWED_ATTACKS)

    @staticmethod
    def __input_attack() -> str:
        """ Asks for user attack input"""
        while True:
            attack_input = input('Select attack:\n'
                                 '\t1 - Paper\n'
                                 '\t2 - Stone\n'
                                 '\t3 - Scissors\n'
                                 '\t(0 - Exit Game)\n'
                                 '\t: ')
            if Player.__is_valid_input_attack(attack_input):
                if attack_input == '0':
                    raise QuitApp
                return ALLOWED_ATTACKS[attack_input]
            print('Incorrect input.')

    def attack(self, enemy: Enemy) -> None:
        """Asks the user to choose the attack.
        Calls the fight method."""
        player_attack = self.__input_attack()
        self.__fight(player_attack, enemy)

    def handle_fight_result(self, fight_result: int, enemy: Enemy) -> None:
        """ Handles results of the fight"""
        if fight_result == 1:
            print('You attacked successfully!')
            self.__on_win_fight(enemy)
        elif fight_result == -1:
            print("You missed!")
            self.decrease_lives()
        elif fight_result == 0:
            print("It's a draw!")

    def __fight(self, player_attack: str, enemy: Enemy) -> None:
        """Resolves player's attack vs enemy's attack"""
        enemy_attack = enemy.attack()
        print(f"Your attack: {player_attack}.  Enemy's attack: {enemy_attack}")
        fight_result = ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]
        self.handle_fight_result(fight_result, enemy)

    def decrease_lives(self) -> None:
        """Decreases player's lives"""
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def on_enemy_down(self):
        """ Adds score on enemy down."""
        print("Congratulation! Enemy down.")
        self.score += POINTS_FOR_KILLING if self.mode == MODE_NORMAL else POINTS_FOR_KILLING * HARD_MODE_MULTIPLIER

    def __on_win_fight(self, enemy: Enemy) -> None:
        """Adds score in case successful fight.
        calls enemy's method to decrease lives."""
        self.score += POINTS_FOR_FIGHT if self.mode == MODE_NORMAL else POINTS_FOR_FIGHT * HARD_MODE_MULTIPLIER
        enemy.decrease_lives()
