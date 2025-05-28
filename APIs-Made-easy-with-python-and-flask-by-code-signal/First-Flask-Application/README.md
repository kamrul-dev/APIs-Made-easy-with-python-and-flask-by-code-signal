# First Flask Appication

# Unit-1

# Running Your First Flask Application
Welcome to your first step on this exciting learning path! Today we'll set the foundation by exploring what an API is, understanding how APIs are pivotal in modern web development, and diving into the Flask web framework, a powerful tool that empowers you to build web applications quickly and efficiently with Python.

# Understanding APIs and Their Importance
An API (Application Programming Interface) is like a bridge that allows different software applications to communicate. This is crucial in web development, where APIs enable web servers and clients (like browsers or mobile apps) to interact.

A web server hosts web applications and delivers content to users. When you visit a website, your browser sends a request to a web server, which responds with the desired content. An API on a web server lets other software interact with it programmatically, often returning data formats like JSON.

APIs enable developers to integrate various functionalities:

A weather app can fetch data from a meteorological service.
An e-commerce site can process payments using a payment gateway's API.
By allowing different software systems to communicate, APIs help developers build modular, maintainable, and scalable applications. Understanding APIs is essential for developing modern web apps.

# What is Flask?
Flask is a lightweight web framework for Python that allows developers to build web applications quickly and efficiently. It is known for its simplicity and flexibility.

Key Features and Why Flask is Popular:

1. Lightweight and Modular: Flask allows you to choose the components you need.
2. Easy to Learn: Flask’s simple and unopinionated design makes it an ideal choice for beginners.
3. Extensible: You can add additional functionalities using Flask extensions.

By the end of this lesson, you will understand the basics to create and run a simple Flask application.


# Setting Up Flask
While you don't need to worry about installation in CodeSignal's environment, it's still important to know how to do it on your local machine.

To install Flask locally, you can use the followin pip command in your terminal:

```
pip install Flask
```

# Initializing a Flask Application
To create a Flask application, start by importing Flask from the flask package and creating an instance of the Flask class:

```
from flask import Flask

#Initialize a Flask app instance
app = Flask(__name__)
```

Here, from flask import Flask imports the Flask class from the flask package. We then create an instance of the Flask class using app = Flask(__name__).

The __name__ variable is a special built-in variable in Python that holds the name of the current module. When a module is run directly, __name__ is set to "__main__", but when it is imported into another module, __name__ is set to the module's name. Flask uses this to determine the root path of the application, helping it locate resources like templates and static files.



# Running the Flask Development Server
Next, we'll add code to start the Flask development server. Add the following lines to your script:

```
#Check if the script is run directly (not imported)
if __name__ == "__main__":
    # Start the Flask development server
    app.run()
```
This code checks if the script is being run directly. If it is, it starts the Flask development server, which helps you test your application during development. By default, the server runs on http://127.0.0.1:5000. Here, 127.0.0.1 (localhost) means it only listens to requests from your own computer, and 5000 is the port number.



#Customizing the IP Address and Port
You can change the IP address and port if needed. For example, to make the server listen on all available IP addresses and use port 5001, update the app.run() method like this:

```
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
```
host="0.0.0.0": This allows the server to accept connections from any IP address.
port=5001: This changes the port number to 5001.
Now, when you run your script, the Flask application will be accessible on http://0.0.0.0:5001.


# Executing Your Flask Application
To run your Flask application, follow these steps:

1. Open your terminal.
2. Navigate to the directory where your script is saved.
3. Run the following command:

```
python filename.py
```
Replace filename.py with the actual name of your Python script file.

Once the Flask development server starts, you will see output indicating the server is running, similar to this:

```
 * Running on http://127.0.0.1:5000
```
This means your Flask application is up and running on http://127.0.0.1:5000!

# Summary and Next Steps
In this lesson, we've covered:

* The basics of what an API is and why they're important.
* An introduction to Flask and its features.
* How to set up Flask.
* Creating and running a simple Flask application.

Now that you have a basic understanding of Flask, it’s time to practice what you've learned. Upcoming practice exercises will help solidify your knowledge by allowing you to create and modify Flask applications.

Remember, practice is key, so make sure to work through the exercises and explore on your own. Happy coding!

==============================================
================================================
================================================

# Task Instructions:
# Welcome to the Flask application development task!
=========================================================

## Now it's time to show off what you've learned.

Your task is to write a Flask application from scratch by following these steps:

1. Initialize a Flask app instance and name it my_app

2. Check if the script is run directly (if __name__ == "__main__":).

3. Start the server on port 6000 using the default host (127.0.0.1).

4. Execute python solution.py in the terminal.

5. Click Run to test the server, then submit your work!

6. If everything is done correctly, you should see the following output: "Flask App is up and running at http://127.0.0.1:6000". Once we see this message, you'll be ready to move on.

=============================