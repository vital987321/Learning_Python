""" User defined Exceptions """

from settings import *



class GameOver(Exception):
    """raised if player lost all lives"""



class EnemyDown(Exception):
    """Raised in case enemy lost all lives"""
    pass


class QuitApp(Exception):
    """Raised if user send command to exit the unfinished game"""

