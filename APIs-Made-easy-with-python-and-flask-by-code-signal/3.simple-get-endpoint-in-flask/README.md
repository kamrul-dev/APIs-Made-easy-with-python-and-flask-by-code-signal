# Creating a Simple GET Endpoint in Flask

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