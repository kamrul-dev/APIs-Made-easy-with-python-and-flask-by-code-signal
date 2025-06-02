
from flask import Flask, jsonify, request


# @app.route('/route', methods=['GET'])
# def function():
#     # Extract the 'parameter_name' query parameter or use 'default_value' if not provided
#     variable = request.args.get('parameter_name', 'default_value')

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    # Extract the 'name' query parameter or use a default value
    name = request.args.get('name', 'Guest')
    
    # Return a JSON response with the query parameter
    return jsonify(message=f"Greetings, {name}! Welcome to the query parameter route.")




