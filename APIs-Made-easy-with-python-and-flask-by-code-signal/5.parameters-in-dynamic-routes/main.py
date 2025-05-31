from flask import Flask, jsonify

# Initialize a Flask app instance
app = Flask(__name__)


@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(message=f"Greetings, {name}! Welcome to the dynamic route.")