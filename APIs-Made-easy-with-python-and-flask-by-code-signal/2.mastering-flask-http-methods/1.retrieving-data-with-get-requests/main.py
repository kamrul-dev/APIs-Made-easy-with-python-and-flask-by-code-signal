from flask import Flask

# Initialize a Flask app instance
app = Flask(__name__)

# Mock database as a list of dictionaries
database = [
    {"id": 1, "username": "cosmo"},
    {"id": 2, "username": "jake"},
    {"id": 3, "username": "emma"}
]

@app.route('/all_users', methods=['GET'])
def get_users():
    # Return the entire user database as JSON
    return jsonify(database)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Loop through the database to find the user with the given ID
    for user in database:
        if user['id'] == user_id:
            # Return the found user as JSON
            return jsonify(user)
    # Return an error message if the user is not found
    return jsonify(error="User not found"), 404