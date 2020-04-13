from flask import Flask, jsonify, request
from flask_cors import CORS
from pandoc.generator import *

app = Flask(__name__)
CORS(app)

exercises = [{'title': globals()[f].__doc__, 'name': f} for f in dir() if f.startswith('generate_')]

@app.route('/')
def exercise_list():
    global exercises
    return jsonify(exercises)

@app.route('/add_question/<name>/<n>/<level>')
def add_question(name, n, level):
    if name not in exercises:
        pass
    function = globals()[name]
    questions = []
    while len(questions) < int(n):
        q = function(int(level))
        if q not in questions:
            questions.append(q)
    return jsonify(questions)

app.run(debug=True, host='0.0.0.0')
