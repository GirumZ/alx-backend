#!/usr/bin/env python3
from flask import Flask, render_template
"""
Simple flask app
"""


app = Flask(__name__)
app.url_map_strict_slashes = False


@app.route('/')
def index() -> str:
    """Index route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
