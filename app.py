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

@app.route('/add_question/<name>/<n>')
def add_question(name, n = 1):
    if name not in exercises:
        pass
    function = globals()[name]
    questions = []
    while len(questions) < int(n):
        q = function()
        if q not in questions:
            questions.append(q)
    return jsonify(questions)
