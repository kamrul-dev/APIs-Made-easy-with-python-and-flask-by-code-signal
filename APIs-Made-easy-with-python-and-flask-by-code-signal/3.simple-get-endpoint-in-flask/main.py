from flask import Flask

# Initialize a Flask app instance
app = Flask(__name__)

# Define a route with a decorator
@app.route('/hello')
def hello():
    # Return a simple string response
    return "Hello, World!"