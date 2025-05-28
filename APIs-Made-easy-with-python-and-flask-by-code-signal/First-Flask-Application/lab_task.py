# TODO: Import the Flask class from the flask package
from flask import Flask

# TODO: Initialize a Flask app instance and call it my_app, remember to pass __name__ as an argument
my_app = Flask(__name__)

# TODO: Check if the script is run directly (not imported)
if __name__ == "__main__":
    # TODO: Start the server on port 6000
    my_app.run(port=6000)
    

# To run the application, use the following command in the terminal:
# python lab_task.py


# Task Instructions:
# Welcome to the Flask application development task!
# =========================================================

# Now it's time to show off what you've learned.

# Your task is to write a Flask application from scratch by following these steps:

# Initialize a Flask app instance and name it my_app

# Check if the script is run directly (if __name__ == "__main__":).

# Start the server on port 6000 using the default host (127.0.0.1).

# Execute python solution.py in the terminal.

# Click Run to test the server, then submit your work!

# If everything is done correctly, you should see the following output: "Flask App is up and running at http://127.0.0.1:6000". Once we see this message, you'll be ready to move on.

########