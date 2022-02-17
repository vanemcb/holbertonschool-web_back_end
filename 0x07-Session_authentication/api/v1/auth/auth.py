#!/usr/bin/env python3
"""
Module Auth class
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method require_auth """

        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[len(path) - 1] != '/':
            path = path + '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Public method authorization_header """

        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method current_user """
        return None

    def session_cookie(self, request=None):
        """ Method that returns a cookie value from a request """

        if request is None:
            return None

        _my_session_id = getenv('SESSION_NAME')
        value_cookie = request.cookies.get(_my_session_id)
        return value_cookie
