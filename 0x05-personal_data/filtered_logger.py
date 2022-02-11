#!/usr/bin/env python3
""" Module function filter_datum """
from typing import List
import re
import logging


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
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        test_dict = {'name': record.name,
                     'levelname': record.levelname,
                     'asctime': record.asctime,
                     'message': record.msg}
        return self.FORMAT % test_dict


def filter_datum(
        fields: List[str], redaction: str, message: str,
        separator: str) -> str:
    """ Function that returns the log message obfuscated """

    for field in fields:
        message = re.sub(
            "{}=.+?{}".format(field, separator), "{}={}{}".format(
                field, redaction, separator), message)

    return message
