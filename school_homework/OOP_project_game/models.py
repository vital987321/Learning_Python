class Participant():
    level: int
    lives: int


class Player(Participant):
    name: str

    def __init__(self, name):
        self.name = name


class Enemy(Participant):
    lives: int
    level: int
