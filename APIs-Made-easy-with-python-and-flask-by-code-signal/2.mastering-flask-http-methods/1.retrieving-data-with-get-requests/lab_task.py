
from flask import Flask, jsonify

# Initialize a Flask app instance
app = Flask(__name__)

# Mock database as a list of dictionaries
database = [
    {"id": 1, "profile_name": "ron"},
    {"id": 2, "profile_name": "hermione"},
    {"id": 3, "profile_name": "harry"}
]

# TODO: Define a route to get all profiles at '/all_profiles'
@app.route('/all_profiles', methods=['GET'])
    # TODO: Return the entire profiles database as JSON
def get_all_profiles():
    return jsonify(database)

# TODO: Define a route at '/profiles' to get a single profile by ID with an int path parameter
@app.route('/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    # TODO: Loop through the database to find the profile with the given ID
    for profile in database:
        if profile['id'] == profile_id:
            # Return the found profile as JSON
            return jsonify(profile)

    # TODO: Return an error message with a 404 status code if the profile is not found
    return jsonify(error='profile not found'), 404














# It's time to show you've mastered retrieving data with GET requests in Flask.

# Your task is to:

# Set up a GET endpoint at the URL /all_profiles to retrieve all profiles from the mock database.
# Set up another GET endpoint at the URL /profiles/<int:profile_id> to retrieve a single profile by ID.
# Here's a generic code example of how to search for an item in a list of dictionaries:

# Python
# Copy to clipboard
# for item in item_list:
#     if item['id'] == item_id:
#         return item