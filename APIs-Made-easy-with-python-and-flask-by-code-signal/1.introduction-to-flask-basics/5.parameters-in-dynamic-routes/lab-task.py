
from flask import Flask, jsonify

# Initialize a Flask app instance
app = Flask(__name__)

# TODO: Define a route with a parameter at the base URL /weather
@app.route('/weather/<city>', methods=['GET'])
# - The route should capture a city parameter from the URL
def get_city(city):
# - The endpoint should support the GET method
    # TODO: Return a JSON response with a dynamic weather message
    return jsonify(message=f"The weather in {city} is sunny.")











# Great job making it this far! You've now reached the final task of this unit. Let's put what you've learned into practice.

# Write a Flask application that defines a dynamic route with a path parameter.

# The dynamic route should:

# Capture a city from the URL path using the /weather base URL.
# Return a JSON response that states the weather forecast for the city, such as:
# "The weather in London is sunny."