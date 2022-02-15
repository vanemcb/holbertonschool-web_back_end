#!/usr/bin/env python3
"""
Module BasicAuth class
"""
from base64 import b64decode
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Returns the decoded value of a Base64 string
        base64_authorization_header """

        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            base_encode = base64_authorization_header.encode('utf-8')
            base_decode64 = b64decode(base_encode)
            decoded = base_decode64.decode('utf-8')
            return decoded
        except Exception:
            return None
