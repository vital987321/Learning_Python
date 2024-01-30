from school_homework.OOP_project_game.game_exceptions import RecordInRecordsError
from school_homework.OOP_project_game.models import Player
from school_homework.OOP_project_game.settings import SCORE_FILE, MAX_RECORDS_NUMBER


def record_file_title_row(name_column_size: int) -> str:
    return f'{"NAME".ljust(name_column_size)}{"MODE".ljust(10)}SCORE\n'


class PlayerRecord:
    name: str
    mode: str
    score: int

    def __init__(self, name: str, mode: str, score: int) -> None:
        self.name = name
        self.mode = mode
        self.score = score

    def __eq__(self, other):
        return self.name == other.name and self.mode == other.mode and self.score == other.score

    def __gt__(self, other):
        return len(self.name) > len(other.name)

    def as_file_row(self, name_column_size: int) -> str:
        return f'{self.name.ljust(name_column_size)}{self.mode.ljust(10)}{self.score}\n'


class GameRecord:
    records: list[PlayerRecord] = []
    mode: str

    def __init__(self, mode: str):
        self.mode = mode
        self.read_records()

    def read_records(self) -> None:
        with open(SCORE_FILE, 'r') as file:
            lines = file.readlines()
        del lines[0]  # remove table title
        for line in lines:
            name, mode, score = line.split()
            self.records.append(PlayerRecord(name, mode, int(score)))

    def _validate_record(self, record: PlayerRecord) -> None:
        """validate record"""
        if record in self.records:
            raise RecordInRecordsError

    def add_record(self, player: Player) -> None:
        player_record = PlayerRecord(player.name, self.mode, player.score)
        try:
            self._validate_record(player_record)
            self.records.append(player_record)
        except RecordInRecordsError:
            raise

    def _sort_records(self) -> list[PlayerRecord]:
        return sorted(self.records, key=lambda x: int(x.score), reverse=True)

    @staticmethod
    def _cut_records(records: list[PlayerRecord]) -> list[PlayerRecord]:
        return records[:MAX_RECORDS_NUMBER]

    @property
    def _prepared_records_to_save(self) -> list[PlayerRecord]:
        records = self._sort_records()
        return self._cut_records(records)

    def save_to_file(self) -> None:
        """save scores to file"""
        records = self._prepared_records_to_save
        name_column_size = len(max(records).name) + 4
        with open(SCORE_FILE, 'w') as file:
            file.write(record_file_title_row(name_column_size))
            for record in records:
                file.write(record.as_file_row(name_column_size))
