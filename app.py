from flask import Flask, render_template, abort
from pathlib import Path

app = Flask(__name__)

PROGRAMS_DIR = Path("DAA")


@app.route("/")
def index():
    files = sorted(
        [f.name for f in PROGRAMS_DIR.iterdir() if f.is_file()]
    )
    return render_template("index.html", files=files)


@app.route("/program/<filename>")
def view_program(filename):
    file_path = PROGRAMS_DIR / filename

    if not file_path.exists():
        abort(404)

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    return render_template(
        "view.html",
        filename=filename,
        code=code
    )


if __name__ == "__main__":
    app.run(debug=True)