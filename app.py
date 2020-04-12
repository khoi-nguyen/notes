from flask import Flask, jsonify, request
from flask_cors import CORS
from pandoc.generator import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def exercise_list():
    return jsonify([
        {
            'title': 'Quadratic Equations',
            'name': 'quadratic_equation',
        }
    ])

@app.route('/add_question/<name>/<n>')
def add_question(name, n = 1):
    function = globals()[f'generate_{name}']
    questions = []
    while len(questions) < int(n):
        q = function()
        if q not in questions:
            questions.append(q)
    return jsonify(questions)
