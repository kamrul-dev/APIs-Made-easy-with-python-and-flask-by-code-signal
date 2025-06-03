# Retrieving Data with GET Requests

Welcome to another milestone in your Flask journey. Throughout this course, we will explore various HTTP methods using a mock database to illustrate practical applications. In this lesson, we will concentrate on using the GET method to retrieve data from a mock database.

By the end of this lesson, you will be able to create Flask endpoints to retrieve data using GET requests, building on the concepts you've already learned. We will also cover how to handle errors and return appropriate status codes to ensure robust and reliable API endpoints.


# Setting Up Flask and Mock Database
Let's go over how to set up a basic Flask application and introduce the mock database we'll be using throughout this course to teach HTTP methods.

```
from flask import Flask

# Initialize a Flask app instance
app = Flask(__name__)

# Mock database as a list of dictionaries
database = [
    {"id": 1, "username": "cosmo"},
    {"id": 2, "username": "jake"},
    {"id": 3, "username": "emma"}
]
```

In this setup, we initialize a Flask application and create a mock database represented as a list of dictionaries. This user database will be the core of our exercises throughout the course, where we will practice retrieving, inserting, editing, and deleting data.


# Defining a Route to Get All Users
Now, let's create an endpoint to retrieve all users from our mock database. We will use the GET method to define this route. Here's the code to define such a route:

```
from flask import jsonify

@app.route('/all_users', methods=['GET'])
def get_users():
    # Return the entire user database as JSON
    return jsonify(database)
```

Explanation:

* Firstly, we define a route that responds to GET requests at the /all_users URL.
* The get_users function is called when a GET request is made to this URL.
* The jsonify(database) function converts the user database (a list of dictionaries) into a JSON response and returns it.

# Accessing GET /all_users
When you run this code and access /all_users, you'll get an HTTP 200 status code (which means success) along with a JSON response containing all users from the mock database:

```
[
    {"id": 1, "username": "cosmo"},
    {"id": 2, "username": "jake"},
    {"id": 3, "username": "emma"}
]
```

# Defining a Route to Get a Single User by ID
Next, we will create an endpoint to retrieve a single user by their ID using a path parameter. Here's how we do it:

```
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Loop through the database to find the user with the given ID
    for user in database:
        if user['id'] == user_id:
            # Return the found user as JSON
            return jsonify(user)
    # Return an error message if the user is not found
    return jsonify(error="User not found"), 404
```
Explanation:

* The `/users` route includes a path parameter `/<int:user_id>` to capture the user's ID from the URL.
* Specifically, the `int:` part ensures that the parameter is treated as an integer. If an incompatible data type is provided, Flask will return a 404 error.
* Then, the `get_user` function takes `user_id` as an argument and searches the database for a user with that ID.
* If the user is found, it returns the user as JSON.
* Otherwise, it returns a JSON error message with a 404 status code.



# Accessing GET /users
For example, if you access /users/2, you will get an HTTP 200 status code along with the following JSON response:

```
{
    "id": 2,
    "username": "jake"
}
```

# Error Handling for Non-existent Users
It's important to handle cases where a user is not found in the database. In the previous section, we included error handling within the get_user function. Here's the relevant code:

```
# Return an error message if the user is not found
return jsonify(error="User not found"), 404
```
This part of the code is executed if the user with the specified ID is not found in the database.

* jsonify(error="User not found") creates a JSON response with an error message.
* The 404 part sets the HTTP status code to 404, which means "Not Found".

In Flask, you can return a response and set its status code by separating them with a comma. This ensures clients know the resource was not found and receive a clear error message.


# Response for Non-existent Users
When a client attempts to access a user ID that does not exist, such as /users/99, the server will respond with an HTTP 404 status code, indicating that the requested resource was not found. The JSON response will contain a descriptive error message:

```
{
    "error": "User not found"
}
```
This response helps clients understand that the specified user ID does not exist in the database and guides them to correct their request accordingly.

# Summary and Preparation for Practice
In this lesson, we unlocked the power of GET requests in Flask, enabling us to effortlessly retrieve data from a mock database. You learned how to:

* Set up a basic Flask application with a mock user database.
* Create an endpoint to fetch all users.
* Create an endpoint to retrieve a specific user by ID.
* Implement error handling for non-existent users to ensure robust and reliable API endpoints.

It's now time to put your newfound knowledge to the test! Dive into the practice exercises where you'll will reinforce your understanding and prepare you for more advanced techniques in future lessons.

Get ready to flex your coding muscles and have some fun exploring the power of Flask!

