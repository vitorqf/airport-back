"""
Step by step to create an API with Flask
Step 1: pip install Flask and import it
Step 2: create a Flask instance
Step 3: run the app
"""

from flask import Flask

app = Flask(__name__)

app.run(debug=True)