from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Mock database with user data
database = [
    {"id": 1, "username": "cosmo"},
    {"id": 2, "username": "jake"},
    {"id": 3, "username": "emma"}
    ]

# Define a route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    # Get the new user data from the request body
    new_user = request.get_json()

    # Validate the new user data
    if "username" not in new_user:
        # Return a 400 Bad Request error if data is invalid
        return jsonify(error="Invalid data"), 400

    # Generate a new ID by finding the maximum existing ID and adding 1
    new_id = max(user['id'] for user in database) + 1
    new_user["id"] = new_id

    # Add the new user to the mock database
    database.append(new_user)
    
    # Return the newly added user as JSON with a status code 201 (Created)
    return jsonify(new_user), 201