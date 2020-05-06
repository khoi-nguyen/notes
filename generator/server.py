from flask import Flask, jsonify, request
from flask_cors import CORS
from generator.algebra import *
from generator.analysis import *
from generator.geometry import *
from solver.algebra import *
from solver.analysis import *
from solver.geometry import *
from solver.mechanics import *
import re

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app)


def get_description(function):
    docstring = globals()[function].__doc__
    levels = re.findall(r"^\s*([1-9]):\s*(.*)$", docstring, re.MULTILINE)
    levels = {int(l[0]): l[1] for l in levels}
    return levels


exercises = [
    {
        "title": globals()[f].__doc__.partition("\n")[0],
        "name": f,
        "levels": get_description(f),
    }
    for f in dir()
    if f.startswith("generate_")
]


@app.route("/")
def exercise_list():
    global exercises
    return jsonify(exercises)


@app.route("/add_question/<name>/<int:n>/<int:level>")
def add_question(name, n, level):
    if name not in exercises:
        pass
    function = globals()[name]
    questions = []
    while len(questions) < n:
        q = function(level)
        if q not in questions:
            questions.append(q)
    return jsonify(questions)


@app.route("/solver", methods=["POST"])
def solver():
    command = request.form["command"]
    return jsonify(eval(command))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
