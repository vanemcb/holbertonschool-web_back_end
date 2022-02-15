#!/usr/bin/env python3
"""
Module BasicAuth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header
        for a Basic Authentication """

        if authorization_header is None or type(authorization_header) != str:
            return None
        if authorization_header[0:6] != 'Basic ':
            return None

        return authorization_header[6:]
