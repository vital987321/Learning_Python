class GameOver(Exception):
    pass


class EnemyDown(Exception):
    pass


class KeyboardInterrupt(Exception):
    pass


class IncorrectUserAttackInput(Exception):
    error_message = 'Incorrect input! User choice must be a number 1 ,2 or 3'


class FightError(Exception):
    pass
