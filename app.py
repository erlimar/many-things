import json
from flask import Flask, jsonify, escape

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello", 200

@app.route('/devs', methods=['GET'])
def devs():
    devs = [
        {
            'name': 'Erlimar',
            'langs': ['C', 'C#', 'C++', 'Rust', 'Pascal', 'PHP', 'JavaScript']
        }
    ]
    return jsonify(devs), 200

@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s!' % escape(name)

if __name__ == '__main__':
    app.run(debug=True)

