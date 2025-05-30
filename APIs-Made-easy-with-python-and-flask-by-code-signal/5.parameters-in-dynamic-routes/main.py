from flask import Flask, jsonify

# Initialize a Flask app instance
app = Flask(__name__)




@app.route('/greet', methods=['GET'])
def greet_default():
    return jsonify(message="Greetings! Welcome to the default greeting.")


@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(message=f"Greetings, {name}! Welcome to the dynamic route.")



@app.route('/greet/<first_name>/<last_name>', methods=['GET'])
def greet_full_name(first_name, last_name):
    return jsonify(message=f"Greetings, {first_name} {last_name}!")

    