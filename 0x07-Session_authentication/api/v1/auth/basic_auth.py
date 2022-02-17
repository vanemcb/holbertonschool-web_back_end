#!/usr/bin/env python3
"""
Module BasicAuth class
"""
from base64 import b64decode
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Returns the user email and password from the
        Base64 decoded value """

        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        string = decoded_base64_authorization_header.split(':')
        return string[0], string[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password """

        if user_email is None or type(user_email) is not str:
            return(None)
        if user_pwd is None or type(user_pwd) is not str:
            return(None)

        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Function that overloads Auth and retrieves the User
        instance for a request """
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            credentials = self.extract_user_credentials(decodeValue)
            user = self.user_object_from_credentials(credentials[0],
                                                     credentials[1])
            return user
        except Exception:
            return None
