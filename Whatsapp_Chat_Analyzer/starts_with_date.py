"""Module that contains a function to identify the beginning of messages"""

import re


def startsWithDate(text):
    """
    Determine wether each new line is a new message beginnning with a date followed by an our.

    Returns:
        [bool]: True in success otherwise False
    """
    # date format m/dd/yy, hour:minutes pm|am -> 12 hour system
    date_pattern = '^(1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])/([0-9]{2}), (1[0-2]|[1-9]):([0-9][0-9]) (\w\w) -'
    result = re.match(date_pattern, text)
    if result:
        return True
    return False
