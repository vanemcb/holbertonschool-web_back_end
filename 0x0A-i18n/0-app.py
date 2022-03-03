#!/usr/bin/env python3
"""
Module basic Flask app
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
