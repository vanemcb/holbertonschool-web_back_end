#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import jsonify
from auth import Auth


AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def message() -> str:
    """ Main route
    """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def create_user(email: str, password: str) -> str:
    """ POST users/
    JSON body:
      - email
      - password
    Return:
      - User object JSON represented
      - 400 if can't create the new User
    """
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    ex




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
