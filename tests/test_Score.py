import os
from pathlib import Path
from assertpy import assert_that
import pytest

import Utils
from Consts import ROOT_DIR
from Score.Score import Score


class TestScore:
    TEST_SCORE_FILE_PATH: Path = Path(f"{ROOT_DIR}/tests/{Utils.SCORES_FILE_NAME}")

    def setup_class(self):
        Score.SCORE_FILE_PATH = TestScore.TEST_SCORE_FILE_PATH

    @pytest.mark.parametrize(
        "score",
        [
            10,
            20,
            30
        ])
    def test_write_score_to_file(self, score: int):
        if os.path.exists(Score.SCORE_FILE_PATH):
            os.remove(Score.SCORE_FILE_PATH)

        Score._write_score(score)

        with open(Score.SCORE_FILE_PATH, 'r') as score_file:
            score_file_lines: list = score_file.readlines()
            assert_that(score_file_lines).is_not_empty()

            first_line: str = score_file_lines[0].strip()
            assert_that(first_line).is_not_empty()
            assert_that(first_line.isnumeric()).is_true()
            assert_that(int(first_line)).is_equal_to(score)

    @pytest.mark.parametrize(
        "score",
        [
            10,
            20,
            30
        ])
    def test_write_score_to_file_override(self, score: int):
        Score._write_score(score)

        with open(Score.SCORE_FILE_PATH, 'r') as score_file:
            score_file_lines: list = score_file.readlines()
            assert_that(score_file_lines).is_not_empty()

            first_line: str = score_file_lines[0].strip()
            assert_that(first_line).is_not_empty()
            assert_that(first_line.isnumeric()).is_true()
            assert_that(int(first_line)).is_equal_to(score)

    @pytest.mark.parametrize(
        "difficulty,current_score",
        [
            (10, 0),
            (20, 35),
            (30, 17)
        ])
    def test_add_score(self, difficulty: int, current_score: int):
        EXPECTED_NEW_SCORE: int = current_score + (difficulty * 3) + 5

        with open(Score.SCORE_FILE_PATH, 'w+') as score_file:
            score_file.write(str(current_score))

        Score.add_score(difficulty)

        with open(Score.SCORE_FILE_PATH, 'r') as score_file:
            score_file_lines: list = score_file.readlines()
            assert_that(score_file_lines).is_not_empty()

            first_line: str = score_file_lines[0].strip()
            assert_that(first_line).is_not_empty()
            assert_that(first_line.isnumeric()).is_true()

            ACTUAL_NEW_SCORE: int = int(first_line)
            assert_that(ACTUAL_NEW_SCORE).is_equal_to(EXPECTED_NEW_SCORE)

    def teardown_class(self):
        if os.path.exists(TestScore.TEST_SCORE_FILE_PATH):
            os.remove(TestScore.TEST_SCORE_FILE_PATH)
