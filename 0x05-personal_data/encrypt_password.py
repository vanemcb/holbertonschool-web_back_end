#!/usr/bin/env python3
""" Module function hash_password """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Function that returns a salted, hashed password,
    which is a byte string """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed
