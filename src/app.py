from flask import Flask, jsonify
from flask_cors import CORS

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
