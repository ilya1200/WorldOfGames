from pathlib import Path
from flask import Flask, render_template
from Score.Score import Score

app = Flask(__name__)
my_dict = dict()


@app.route('/')
def index() -> str:
    SCORE_FILE: Path = Score.SCORE_FILE_PATH

    try:
        with open(SCORE_FILE, 'r') as score_file:
            score_file_lines: list = score_file.readlines()
            first_line_raw: str = score_file_lines[0]
            first_line: str = first_line_raw.strip()
            score: int = int(first_line)
            return render_template('index.html', SCORE=score)
    except (ValueError, IndexError, FileNotFoundError):
        return render_template('error.html', ERROR="Failed to read score")


app.run(port=5001, debug=True)

if __name__ == "__main__":
    app.run()
