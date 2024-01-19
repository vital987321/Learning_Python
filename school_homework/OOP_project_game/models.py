from game_exceptions import *
from settings import *
from random import randint


class Participant():
    level: int
    lives: int

    def attack(self):
        pass


class Enemy(Participant):
    def __int__(self):
        self.lives = ENEMY_LIVES

    def attack(self) -> str:
        return ALLOWED_ATTACKS[randint(1, 3)]

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()


class Player(Participant):
    name: str
    score: int

    def __init__(self, name):
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    def attack(self, enemy: Enemy):
        while True:
            try:
                player_choice = input('Select attack:\n\t1 - Paper\n\t2 - Stone\n\t3 - Scissors')
                if player_choice in ('1', '2', '3'):
                    player_attack = ALLOWED_ATTACKS[player_choice]
                    break
                else:
                    raise IncorrectUserAttackInput()
            except (IncorrectUserAttackInput):
                print(IncorrectUserAttackInput.error_message)
        fight_result = self.fight(player_attack, enemy)
        if fight_result == 1:
            print('You attacked successfully!')
            self.on_win_fight(enemy)
        elif fight_result == -1:
            print("You missed!")
            self.decrease_lives()
        elif fight_result == 0:
            print("It's a draw!")
        else:
            raise FightError

    def fight(self, player_attack: str, enemy: Enemy):
        enemy_attack = enemy.attack()
        print(f'Your attack: {player_attack}.  Enemy attack: {enemy_attack}')
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

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver()

    def on_win_fight(self, enemy: Enemy):
        self.score += POINTS_FOR_FIGHT
        enemy.decrease_lives()
