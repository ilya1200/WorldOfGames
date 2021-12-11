from pathlib import Path

import Utils
from Consts import ROOT_DIR


class Score:
    SCORE_FILE_PATH = Path(f"{ROOT_DIR}/Score/{Utils.SCORES_FILE_NAME}")

    @staticmethod
    def _read_score() -> int:
        Score.SCORE_FILE_PATH.touch(exist_ok=True)
        with open(Score.SCORE_FILE_PATH, 'r') as score_file:
            score_file_lines: list = score_file.readlines()
            score: int = int(score_file_lines[0].strip()) if score_file_lines else 0
            return score

    @staticmethod
    def _write_score(score: int) -> None:
        with open(Score.SCORE_FILE_PATH, 'w+') as score_file:
            score_file.write(str(score))

    @staticmethod
    def add_score(difficulty: int) -> None:
        CURRENT_SCORE = Score._read_score()

        POINTS_OF_WINNING: int = (difficulty * 3) + 5
        NEW_SCORE: int = CURRENT_SCORE + POINTS_OF_WINNING

        Score._write_score(NEW_SCORE)


Score.add_score(5)
