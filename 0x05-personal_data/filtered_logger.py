#!/usr/bin/env python3
""" Module function filter_datum """
from typing import List
import re


def filter_datum(
        fields: List[str], redaction: str, message: str,
        separator: str) -> str:
    """ Function that returns the log message obfuscated """

    for field in fields:
        message = re.sub(
            "{}=.+?{}".format(field, separator), "{}={}{}".format(
                field, redaction, separator), message)

    return message
