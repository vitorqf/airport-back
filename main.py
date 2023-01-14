from db import Parts

"""
Step by step to create an API with Flask
Step 1: pip install Flask and import it
Step 2: create a Flask instance
Step 3: run the app
"""

from flask import Flask, make_response, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False 

# Decorator from flask import
@app.route('/parts', methods=['GET'])
def get_parts():
    # It's important to use flask make_response function to return a HTTP response. To handle data like raw list its also interesting to use jsonify function function to handle it as a json
    return make_response(jsonify(
        message='Part list',
        data=Parts
    ))

@app.route('/parts/create', methods=['POST'])
def create_new_part():
    part = request.json
    Parts.append(part)
    return make_response(jsonify(
        message='Part successfully created!',
        part=part
    ))

app.run(debug=True)