#!/usr/bin/env python3
"""0-app module for i18n"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """index page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
