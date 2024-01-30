""" Constants and settings used in the project """

ALLOWED_ATTACKS = {'1': 'Paper',
                   '2': 'Stone',
                   '3': 'Scissors',
                   '0': 'Exit Game'}
MODES = {'1': "Normal",
         '2': "Hard"}
MODE_NORMAL = 'Normal'
MODE_HARD = 'Hard'
PLAYER_LIVES = 2
POINTS_FOR_FIGHT = 1
POINTS_FOR_KILLING = 5
MAX_RECORDS_NUMBER = 10
HARD_MODE_MULTIPLIER = 2
SCORE_FILE = 'scores.txt'
PAPER = 'Paper'
STONE = 'Stone'
SCISSORS = 'Scissors'
ATTACK_PAIRS_OUTCOME = {(PAPER, PAPER): 0,
                        (PAPER, STONE): 1,
                        (PAPER, SCISSORS): -1,
                        (STONE, PAPER): 1,
                        (STONE, STONE): 0,
                        (STONE, SCISSORS): -1,
                        (SCISSORS, PAPER): 1,
                        (SCISSORS, STONE): -1,
                        (SCISSORS, SCISSORS): 0}
