# Launching a Falsk Application with Gunicorn


# Launching a Flask Application with Gunicorn
Welcome to another lesson in our course on building APIs with Python and Flask. Previously, you learned how to set up a simple Flask application and run it using the built-in Flask server. Now, let's take our Flask application to the next level by introducing Gunicorn, a more robust way to serve our application.


# Recap: Setting Up a Simple Flask App
Before we start using Gunicorn, let's quickly recap how to set up a simple Flask application. Here’s a basic app that we covered in the previous lesson:

```
from flask import Flask  
```

# Initialize a Flask app instance
app = Flask(__name__)

# Note: We won't need the app.run() block when using Gunicorn
In this code:

1. We import the Flask class from the flask module.
2. We create an instance of the Flask class and call it app.

When using Gunicorn, there's no need for the if __name__ == "__main__": app.run() block, which was necessary when using the built-in Flask server.