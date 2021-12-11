from pathlib import Path

import Utils
from Consts import ROOT_DIR


class Score:
    SCORE_FILE_PATH: Path = Path(f"{ROOT_DIR}/Score/{Utils.SCORES_FILE_NAME}")

    @staticmethod
    def _read_score() -> int:
        """
        Reads the score from the first line in Score.txt file.
        If that file does not exist, it will be created empty

        :return: The score or 0 if the first line is empty
        """
        Score.SCORE_FILE_PATH.touch(exist_ok=True)
        with open(Score.SCORE_FILE_PATH, 'r') as score_file:
            score_file_lines: list = score_file.readlines()
            score: int = int(score_file_lines[0].strip()) if score_file_lines else 0
            return score

    @staticmethod
    def _write_score(score: int) -> None:
        """
        Writes the score into Score.txt and overrides its existing content

        :param score The score to be written into the file
        """
        with open(Score.SCORE_FILE_PATH, 'w+') as score_file:
            score_file.write(str(score))

    @staticmethod
    def add_score(difficulty: int) -> None:
        """
        Calculate the new score and write it into Score.txt
        :param difficulty - the additional score depends on the difficult
        """
        CURRENT_SCORE: int = Score._read_score()

        POINTS_OF_WINNING: int = (difficulty * 3) + 5
        NEW_SCORE: int = CURRENT_SCORE + POINTS_OF_WINNING

        Score._write_score(NEW_SCORE)



