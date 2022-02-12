#!/usr/bin/env python3
""" Module function filter_datum """
from typing import List
import re
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        " Method to filter values in incoming log records using filter_datum "

        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(
        fields: List[str], redaction: str, message: str,
        separator: str) -> str:
    """ Function that returns the log message obfuscated """

    for field in fields:
        message = re.sub(
            "{}=.+?{}".format(field, separator), "{}={}{}".format(
                field, redaction, separator), message)

    return message


def get_logger() -> logging.Logger:
    """ Function that returns a logging.Logger object """

    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(stream_handler)

    return log
