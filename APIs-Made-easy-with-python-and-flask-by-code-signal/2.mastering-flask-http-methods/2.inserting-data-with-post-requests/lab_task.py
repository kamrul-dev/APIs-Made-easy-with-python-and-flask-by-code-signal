from flask import Flask, request, jsonify

# Initialize a Flask app instance
app = Flask(__name__)

# Mock database as a list of dictionaries
database = [
    {"id": 1, "title": "Understanding Flask"},
    {"id": 2, "title": "Advanced Flask Patterns"},
    {"id": 3, "title": "Deploying Flask Applications"}
]

# Define a route at `/articles` to create a new article
@app.route('/article', methods=['POST'])
def create_article():
    # TODO: Extract the new article data from the request body using request.get_json()
    new_article = request.get_json()
    
    # TODO: Validate the new article data to include the 'title' field
    if "title" not in new_article:
        # TODO: Return an error message and a 400 status code if 'title' is missing
        return jsonify(error="Invalid data"), 400
    
    # TODO: Generate a new ID by finding the maximum existing ID and adding 1
    new_id = max(article['id'] for article in database) + 1
    new_article['id'] = new_id

    # TODO: Add the new article to the mock database
    database.append(new_article)

    # TODO: Return the newly added article as JSON with a status code 201 (Created)
    return jsonify(new_article), 201




#     The task now is to write a POST endpoint for adding a new article to a mock database.

# This endpoint should:

# Accept JSON data with title.
# Validate the presence of the title field.
# Generate a unique ID for the new article.
# Append the new article to the mock database.
# Return the newly added article along with a status code of 201 (Created).
# Example of generating a new ID and appending an item:

# Python
# Copy to clipboard
# new_id = max(item['id'] for item in database) + 1
# new_item['id'] = new_id
# database.append(new_item