# Working with URL Query Parameters

# UNIT-6
Welcome to this lesson on working with URL Query Parameters in Flask! In previous lessons, you learned how to build dynamic routes using path parameters. Now, we're going to take it a step further by understanding and implementing URL Query Parameters in your Flask applications.


# Understanding URL Query Parameters

URL Query Parameters are parameters appended to the URL to pass additional information to the server. They follow the ? symbol in a URL and are separated by the & symbol. For example:

```
/greet?name=John&age=25
```
In this example, name and age are query parameters with values John and 25, respectively. Query parameters allow users to interact with and customize web server responses without changing the server-side code.


# Path vs Query Parameters
Both types of parameters pass data to web applications, but they serve different roles and are used in distinct contexts.

Path parameters are integral to the URL and are used to pinpoint specific resources. For instance, in the URL /users/123, 123 is a path parameter that identifies a particular user. Use path parameters for essential, hierarchical data that define the resource's identity.

Query parameters provide additional information and follow a ? in the URL. For example, in /products?category=books&sort=price_asc, category and sort are query parameters. They are ideal for optional data that customizes the request, like filters and sorting.

Understanding the differences helps you choose the right approach: path parameters for required, resource-specific data and query parameters for optional, customizable data.


# Extracting Query Parameters from Request
Flask makes it easy to handle URL query parameters through the request module. Here's a simple example to show how you can extract query parameters using request.args.get():

```
from flask import request

@app.route('/route', methods=['GET'])
def function():
    # Extract the 'parameter_name' query parameter or use 'default_value' if not provided
    variable = request.args.get('parameter_name', 'default_value')
```

In this example, we import the request module from Flask to work with query parameters. You don't need to change the route decorator at all. Just extract the value of the query parameter parameter_name using request.args.get('parameter_name', 'default_value'), which also sets a default value if no parameters is passed. Let's break it down:

* request: Contains all the data associated with the HTTP request made to the server.
* args: A dictionary-like structure within the request object that contains URL query parameters.
* get: Retrieves the value associated with the specified key (query parameter name) in args, with an optional default value if the key is not present.


# Creating a Query Parameter Route
Now let's create a Flask route that accepts query parameters and responds with a JSON message.

```
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    # Extract the 'name' query parameter or use a default value
    name = request.args.get('name', 'Guest')
    
    # Return a JSON response with the query parameter
    return jsonify(message=f"Greetings, {name}! Welcome to the query parameter route.")
```

Within this route function, request.args.get('name', 'Guest') is used to extract the name query parameter, defaulting to 'Guest' if it is not provided. Finally, the function returns a JSON object that includes the value of the name parameter.


# Accessing the Query Parameter Route
When you navigate to /greet?name=John, Flask captures John as the name parameter and returns a response like this:

```
{
    "message": "Greetings, John! Welcome to the query parameter route."
}
```
If you navigate to /greet without providing the name query parameter, Flask will use the default value and return a response like this:

```
{
    "message": "Greetings, Guest! Welcome to the query parameter route."
}
```


# Using Multiple Query Parameters
You can also handle multiple query parameters in a single route. For example, let's create a Flask route that accepts both name and age query parameters:

```
@app.route('/greet', methods=['GET'])
def greet_name_age():
    # Extract 'name' and 'age' query parameters with default values
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'unknown')

    return jsonify(message=f"Greetings, {name}! You are {age} years old.")
```

Navigating to /greet?name=John&age=25 would result in a response like this:

```
{
    "message": "Greetings, John! You are 25 years old."
}
```


# Use Cases for URL Query Parameters
Query parameters are highly useful in web applications. Here are some common use cases:

* Search Functionality: Implement search endpoints that take search terms as query parameters
    * `/search?term=shoes`
* Filtering Results: Filter results based on criteria like age, category, etc.
    * `/users?age=25`
* Customization: Customize responses based on user preferences
    * `/dashboard?theme=dark`
These examples demonstrate how query parameters make your web applications more flexible and user-friendly.


# Review and Practice Overview
In this lesson, you learned how to work with URL Query Parameters in Flask. We understood what query parameters are, and implemented them in a Flask route. Through the example, you saw how to extract query parameters using request.args and handle cases where a required parameter is not provided.

Now it's time to practice! The upcoming exercises will give you a chance to apply what you've learned and solidify your understanding of query parameters in Flask. Great job on reaching this far, and keep up the excellent work!

Let's get practicing!


# Lab Task Instructions
## ==============================

Your task is to write a Flask application that defines a route that accepts URL query parameters.

1. Define an endpoint at /welcome.
2. The function should extract the name query parameter.
3. If the name query parameter is not provided, it should default to 'Visitor'.
4. The route should return a JSON response with the message: "Welcome, [name]! Enjoy your stay on this route."