from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/users')
def hello_world():
    return jsonify({'userId': 42}), 200


@app.route('/new/users')
def hello_world1():
    return jsonify({'userId': 100}), 200


if __name__ == '__main__':
    app.run()
