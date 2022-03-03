#!/usr/bin/env python3
"""
Module basic Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """Class Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """Index page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
