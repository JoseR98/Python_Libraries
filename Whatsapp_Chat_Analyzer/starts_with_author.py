"""Module that contains a function to identify the Author of messages"""

import re


def startsWithAuthor(text):
    """
    Detect Author in the message.

    Returns:
        [bool]: True in success otherwise False
    """
    # author format -> author_name: message
    patterns = [
        '( [\w]+):',                        # First Name
        '( [\w]+[\s]+[\w]+):',              # First Name + Last Name
        '( [\w]+[\s]+[\w]+[\s]+[\w]+):'    # First Name + Middle Name + Last Name
    ]
    pattern = '^' + '|'.join(patterns)
    result = re.match(pattern, text)
    if result:
        return True
    return False
