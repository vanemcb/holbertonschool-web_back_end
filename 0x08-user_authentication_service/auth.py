#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method that checks if a user already exists
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except Exception:
            passw = _hash_password(password)
            return self._db.add_user(email, passw)

    def valid_login(self, email: str, password: str) -> bool:
        """Function that locates a user by email and checks
        the password
        """
        try:
            self._db.find_user_by(email=email)
        except Exception:
            if bcrypt.checkpw(password, _hash_password(password)):
                return True
        return False


def _hash_password(password: str) -> bytes:
    """Function that returns a salted, hashed password,
    which is a byte string
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
