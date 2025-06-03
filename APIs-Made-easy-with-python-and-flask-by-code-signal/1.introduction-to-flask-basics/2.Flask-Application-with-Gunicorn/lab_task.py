from flask import Flask  

# TODO: Change the Flask instance name from 'app' to 'my_app' 
my_app = Flask(__name__)

# With the change done, use the following updated command to launch it:
# gunicorn solution:my_app



















# We've just explored how to set up a Flask application using Gunicorn. Now, it's time to put that knowledge into practice.

# Give us a few seconds to set up the environment, then execute the following command in the terminal.

# Bash
# Copy to clipboard
# gunicorn solution:app
# After that, click on Run, and we will test if the server is running correctly.


# =======================

# Task Instructions
# =======================

# Great job setting up your Flask application with Gunicorn! Now, let's make a small modification to understand the flexibility in naming conventions.

# 1. Change the Flask app instance name from app to my_app in the code.
# 2. Update the Gunicorn command to gunicorn solution:my_app to reflect this change.

# This exercise will help you see how flexible Flask can be in naming your app instance.


# 3. Now, let's modify the command used to launch the app with Gunicorn. This will help you understand how to specify the IP address and port number for your server. Change the command to bind (-b) the server to all IP addresses (0.0.0.0) on port 7000.
