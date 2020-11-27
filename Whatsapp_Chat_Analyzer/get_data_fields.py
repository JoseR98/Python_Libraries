"""Module that contains a function to get the fields for each message"""

from starts_with_author import startsWithAuthor


def getDataFields(text):
    """[summary]

    Args:
        text (str): line of text in the whatsapp chat

    Returns:
        [str]: returns the fields date, time, author and message parsed from the text
    """
    # text example -> 4/7/20, 12:44 pm - Dairo Facundo: ahorita le hecho ojo a ver si veo algo

    split_info = text.split('-')
    date, time = split_info[0].split(',')
    message = ' '.join(split_info[1:])

    if startsWithAuthor(message):
        split_message = message.split(': ')
        author = split_message[0]
        message = ' '.join(split_message[1:])
    else:
        author = None
    return date, time, author, message
