# Creating a Simple GET Endpoint in Flask

# UNIT-3
Welcome to this lesson on creating a simple GET endpoint in Flask. In our previous lessons, you've learned how to set up and run a Flask application. Now, we'll dive into routing, a fundamental concept in web development.


# What is Routing?
Routing is the mechanism that directs web traffic to different parts of a web application. When you type a URL in your browser, routing determines which part of the application should handle that request.

For example, when you navigate to https://codesignal.com/learn, the routing mechanism of the CodeSignal website directs you to the learning section and fetches the relevant data to display. In this URL, https://codesignal.com refers to the domain of the website, which is sometimes called the root, and /learn is the specific path that determines which data and content should be fetched and rendered on the page.

In Flask, routing allows you to map URLs to specific functions in your code, making it easier to manage and expand your web application.


# Recap: Instantiating a Flask App
Before we create a route, let's briefly revisit how to set up a basic Flask application. This was covered in our first lesson, but here's a quick reminder.

```
from flask import Flask

# Initialize a Flask app instance
app = Flask(__name__)
In this snippet, we import the Flask class from the flask module and create an instance of it called app. This instance will be used to configure routes and handle HTTP requests.
```


# Introducing Routes and Decorators
A route in Flask is essentially a URL pattern that the web application responds to. We use decorators like @app.route to define these routes.

```
#Define a route with a decorator
@app.route('/hello')
def hello():
    # Return a simple string response
    return "Hello, World!"
```
In this example, the line @app.route('/hello') is a decorator that tells Flask to execute the hello function when the /hello URL is accessed.

A decorator in Python is a special type of function used to modify the behavior of another function. In this case, @app.route modifies hello so that it reacts to web requests made to the /hello URL.

The function hello handles the request and returns a simple string as the response. If you access http://localhost:5000/hello (assuming you are running on this IP and port), you will receive the text "Hello, World!".

# HTTP Method in Flask
Flask supports multiple HTTP methods, such as GET, POST, PUT, and DELETE. These methods define the type of action you want to perform for a given URL. If you do not specify a method to your route, Flask will use GET as default.


# Use Cases of GET Method
The GET method is one of the most common HTTP methods used in web development, primarily for retrieving data from the server. Here are a few real-world examples:

1. Viewing a Webpage: When you type a URL in your browser, it sends a GET request to the server to fetch and display the webpage.
2. Fetching Data: Many APIs use the GET method to fetch data, such as retrieving a list of users or fetching the details of a specific item.

While GET is great for retrieving data, other HTTP methods (like POST, PUT, and DELETE) are used for actions like updating or deleting data. We'll explore these in future lessons.

As we saw in the previous code snippet, if you do not specify a method for your route, Flask will use GET by default.


# Defining a GET Method Endpoint
To explicitly specify a method for a route, you can use the methods parameter in the @app.route decorator. Below is an example demonstrating how to create a GET endpoint.

```
# Define a GET endpoint
@app.route('/greet', methods=['GET'])
def get_endpoint():
    # Return a string
    return "Hello! You have reached the GET endpoint!"
```
In this code, @app.route('/greet', methods=['GET']) tells Flask to only allow GET requests on the /greet URL, ensuring that the get_endpoint function is called to handle the request and return a simple string response.


# Accessing an Endpoint
To verify your endpoint, you can use a web browser our another tool to navigate to http://your_ip_and_port + /greet and you should see this response:

```
Hello! You have reached the GET endpoint!
```
Additionally, the server will respond with a status code of 200 OK, indicating that the request was successfully processed.

# Summary and Next Steps
In this lesson, you learned how to create a simple GET endpoint in Flask. We introduced the concept of routing, revisited setting up a basic Flask application, and then created a GET endpoint that returns a greeting message. We also discussed how to access your endpoint and examined the common use cases for the GET method.

Now that you understand the basics of creating GET endpoints, you can move on to the practice exercises to solidify your knowledge. These exercises will help you apply what you’ve learned and prepare you for more advanced concepts in Flask web development.



# Lab Task Instructions
=============================

1. Write a Flask application that defines a GET endpoint with a fun twist:
2. Define the GET endpoint at the path /funny.
3. It should return the string: "Why don't scientists trust atoms? Because they make up everything!".