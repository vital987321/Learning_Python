from school_homework.OOP_project_game.game_exceptions import WhiteSpaceInputError, EmptyInputError
from school_homework.OOP_project_game.settings import MODES, ALLOWED_ATTACKS


def validate_name(name: str) -> None:
    """Validates user input name"""

    if ' ' in name:
        raise WhiteSpaceInputError
    elif not name:
        raise EmptyInputError


def get_allowed_options(options_dict: dict) -> tuple:
    return tuple(options_dict.keys())


def is_valid_input_mode(mode_input: str) -> bool:
    """Validates mode input"""
    return mode_input in get_allowed_options(MODES)


def is_valid_menu_input(menu_input: str) -> bool:
    """ Validates menu user input"""
    return menu_input in get_allowed_options(ALLOWED_ATTACKS)


def is_valid_input_attack(attack_input: str) -> bool:
    """ Validates attack input"""
    return attack_input in get_allowed_options(ALLOWED_ATTACKS)
