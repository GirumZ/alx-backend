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
    user = request.args.get("login_as")
    if user:
        lang = users.get(int(user)).get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    headers = request.headers.get("locale")
    if headers:
        return headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ Gets the timezone"""

    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """ renders the index page"""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
