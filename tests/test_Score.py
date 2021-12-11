import os
from pathlib import Path
from assertpy import assert_that
import pytest

import Utils
from Consts import ROOT_DIR
from Score.Score import Score


class TestScore:
    TEST_SCORE_FILE_PATH = Path(f"{ROOT_DIR}/tests/{Utils.SCORES_FILE_NAME}")

    @pytest.mark.parametrize(
        "score",
        [
            10,
            20,
            30
        ])
    def test_write_score_to_file(self, score: int):
        Score.SCORE_FILE_PATH = TestScore.TEST_SCORE_FILE_PATH

        if os.path.exists(Score.SCORE_FILE_PATH):
            os.remove(Score.SCORE_FILE_PATH)

        Score._write_score(score)

        with open(Score.SCORE_FILE_PATH, 'r') as score_file:
            score_file_lines: list = score_file.readlines()
            assert_that(score_file_lines).is_not_empty()

            first_line = score_file_lines[0].strip()
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
        Score.SCORE_FILE_PATH = TestScore.TEST_SCORE_FILE_PATH

        Score._write_score(score)

        with open(Score.SCORE_FILE_PATH, 'r') as score_file:
            score_file_lines: list = score_file.readlines()
            assert_that(score_file_lines).is_not_empty()

            first_line = score_file_lines[0].strip()
            assert_that(first_line).is_not_empty()
            assert_that(first_line.isnumeric()).is_true()
            assert_that(int(first_line)).is_equal_to(score)

    def teardown_class(self):
        if os.path.exists(TestScore.TEST_SCORE_FILE_PATH):
            os.remove(TestScore.TEST_SCORE_FILE_PATH)
