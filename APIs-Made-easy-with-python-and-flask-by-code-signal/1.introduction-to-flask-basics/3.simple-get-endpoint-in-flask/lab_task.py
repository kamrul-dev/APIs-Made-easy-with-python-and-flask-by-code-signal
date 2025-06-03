from flask import Flask

# Initialize a Flask app instance
app = Flask(__name__)

# TODO: Define a GET endpoint at the path /funny
@app.route('/funny', methods=['GET'])
    # TODO: The endpoint should return the string:
def get_funny():
    # "Why don't scientists trust atoms? Because they make up everything!"
     return "Why don't scientists trust atoms? Because they make up everything!"




# Write a Flask application that defines a GET endpoint with a fun twist:

# Define the GET endpoint at the path /funny.
# It should return the string: "Why don't scientists trust atoms? Because they make up everything!".