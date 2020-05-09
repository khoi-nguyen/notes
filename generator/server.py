from flask import Flask, jsonify, request
from flask_cors import CORS
from pandoc.filters.helpers import context_from_pkg
from re import findall, MULTILINE

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app)


def get_description(function):
    docstring = function.__doc__
    levels = findall(r"^\s*([1-9]):\s*(.*)$", docstring, MULTILINE)
    levels = {int(l[0]): l[1] for l in levels}
    return levels


context = context_from_pkg("generator")
exercises = [
    {
        "title": function.__doc__.partition("\n")[0],
        "name": name,
        "levels": get_description(function),
    }
    for name, function in context.items()
    if name.startswith("generate_")
]


@app.route("/")
def exercise_list():
    global exercises
    return jsonify(exercises)


@app.route("/add_question/<name>/<int:n>/<int:level>")
def add_question(name, n, level):
    global context
    if name not in exercises:
        pass
    function = context[name]
    questions = []
    while len(questions) < n:
        q = function(level)
        if q not in questions:
            questions.append(q)
    return jsonify(questions)


@app.route("/solver", methods=["POST"])
def solver_route():
    context = context_from_pkg("solver")
    command = request.form["command"]
    try:
        result = eval(command, globals(), context)
    except (
        AttributeError,
        IndentationError,
        IndexError,
        KeyError,
        NameError,
        SyntaxError,
        TabError,
        TypeError,
        ValueError,
        ZeroDivisionError,
    ) as detail:
        result = ("Error", str(detail))
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
