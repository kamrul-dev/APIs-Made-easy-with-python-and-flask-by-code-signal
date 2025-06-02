
from flask import Flask, jsonify, request

# Initialize a Flask app instance
app = Flask(__name__)

# Define an endpoint at '/welcome'
@app.route('/welcome', methods=['GET'])
def get_welcome():
    # TODO: Extract the query parameter 'name' and set the default value to 'Visitor'
    name = request.args.get('name', 'Visitor')
    # TODO: Use the parameter in the response
    return jsonify(message=f"Welcome, {name}! Enjoy your stay on this route.")


















# Your task is to write a Flask application that defines a route that accepts URL query parameters.

# Define an endpoint at /welcome.
# The function should extract the name query parameter.
# If the name query parameter is not provided, it should default to 'Visitor'.
# The route should return a JSON response with the message: "Welcome, [name]! Enjoy your stay on this route."