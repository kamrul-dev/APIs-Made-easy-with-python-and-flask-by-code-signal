from flask import Flask, jsonify

# Initialize a Flask app instance
app = Flask(__name__)

# Endpoint that returns JSON data
@app.route('/greet', methods=['GET'])
def json_message():
    # TODO: Return a JSON response with a message field
    return jsonify(message="Hey there! This is a JSON response!")






# from flask import Flask, jsonify

# # Initialize a Flask app instance
# app = Flask(__name__)

# # Define a route that returns JSON data
# @app.route('/greet', methods=['GET'])
# def json_message():
#     # TODO: Return a JSON response with an additional field "status" containing the value "Success"
#     return jsonify(message="Hey there! This is a JSON response!", status="Success")



