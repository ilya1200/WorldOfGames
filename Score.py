import logging
from pathlib import Path

from Consts import ROOT_DIR, LOGGING_FORMAT, PATH_TO_LOG_FILE

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Score:
    SCORE_FILE_PATH: Path = Path(f"{ROOT_DIR}/Scores.txt")

    @staticmethod
    def _read_score() -> int:
        """
        Reads the score from the first line in Score.txt file.
        If that file does not exist, it will be created empty

        :return: The score or 0 if the first line is empty
        """
        Score.SCORE_FILE_PATH.touch(exist_ok=True)

        with open(Score.SCORE_FILE_PATH, 'r') as score_file:
            logger.debug(f"Opened Scores files for reading: {Score.SCORE_FILE_PATH}")
            score: int = 0

            score_file_lines: list = score_file.readlines()
            if not score_file_lines:
                # Score.txt is empty
                logger.debug(f"The file {Score.SCORE_FILE_PATH} it empty. Score: {score}")
                return score

            # Score.txt has content, read and parse the first line to retrieve the score
            first_line_raw: str = score_file_lines[0]
            logger.debug(f"Read the first line from the file {Score.SCORE_FILE_PATH}. Content: {first_line_raw}")
            first_line: str = first_line_raw.strip()

            try:
                score = int(first_line)
            except ValueError as e:
                ERR_MSG: str = f"Expected to find an int score number on the first line in the file: {Score.SCORE_FILE_PATH}. Actual: {first_line}"
                if not first_line.isnumeric():
                    logger.error(ERR_MSG)
                raise e
            else:
                logger.debug(f"Read score:{score} from the file {Score.SCORE_FILE_PATH}")
            return score

    @staticmethod
    def _write_score(score: int) -> None:
        """
        Writes the score into Score.txt and overrides its existing content

        :param score The score to be written into the file
        """
        logger.debug(f"score: {score}")
        with open(Score.SCORE_FILE_PATH, 'w+') as score_file:
            logger.debug(f"Opened Scores files for writing: {Score.SCORE_FILE_PATH}")
            score_file.write(str(score))
            logger.debug(f"Wrote the score:{score} into the file: {Score.SCORE_FILE_PATH}")

    @staticmethod
    def add_score(difficulty: int) -> None:
        """
        Calculate the new score and write it into Score.txt
        :param difficulty - the additional score depends on the difficult
        """
        logger.debug(f"difficulty: {difficulty}")

        CURRENT_SCORE: int = Score._read_score()
        logger.info(f"The current score: {CURRENT_SCORE}")

        POINTS_OF_WINNING: int = (difficulty * 3) + 5
        logger.debug(f"POINTS_OF_WINNING: {POINTS_OF_WINNING}")

        NEW_SCORE: int = CURRENT_SCORE + POINTS_OF_WINNING
        logger.debug(f"The new score: {NEW_SCORE}")

        Score._write_score(NEW_SCORE)
        logger.info(f"Written the new score: {NEW_SCORE} into file")


