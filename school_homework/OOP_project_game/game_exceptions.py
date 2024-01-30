""" User defined Exceptions """


class GameOver(Exception):
    """raised if player lost all lives"""


class EnemyDown(Exception):
    """Raised in case enemy lost all lives"""
    pass


class QuitApp(Exception):
    """Raised if user send command to exit the unfinished game"""


class WhiteSpaceInputError(Exception):
    """ Raised if user input contains white spaces"""


class EmptyInputError(Exception):
    """ Raised if user input is an empty string"""
