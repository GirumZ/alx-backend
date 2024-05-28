#!/usr/bin/env python3
from flask import Flask, render_template
"""
Basic flask app
"""


app = Flask(__name__)
app.url_map_strict_slashes = False


@app.route('/')
def index() -> str:
    """
    A route for the index page
    """
    return render_template('0-index.html')
