#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import jsonify


@app.route('/', methods=['GET'], strict_slashes=False)
def message() -> str:
    """ Main route
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
