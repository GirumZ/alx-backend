#!/usr/bin/env python3
"""Basic flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


class Config:
    """Configration class"""

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request() -> None:
    """ Runs before other requestes"""

    g.user = get_user()


def get_user() -> Union[Dict, None]:
    """ Gets the user"""

    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@babel.localeselector
def get_locale() -> str:
    """ Selectes the best match for translation"""

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ renders the index page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
