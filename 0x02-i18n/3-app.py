#!/usr/bin/env python3
"""2-app module for i18n"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)

babel = Babel(app)


class Config:
    """configuration class for babel defaults"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """choose the best match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
