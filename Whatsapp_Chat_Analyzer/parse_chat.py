"""Module that parses data from whatsapp chat file and store it"""

from starts_with_date import startsWithDate
from get_data_fields import getDataFields

parsedData = [] # save parsed data to convert it to a data frame
conversation_file = './whatsapp_chat.txt' 
with open(conversation_file, encoding="utf-8") as fp:
    messageBuffer = [] # intermediate storage for multi-line messages
    date, time, author = None, None, None # keep track the data for each message
    
    while True:
        line = fp.readline() 
        if not line:
            break
        line = line.strip()
        if startsWithDate(line): # Beginning of a new message
            # check for multi-line messages of previous messages.
            if len(messageBuffer) > 0: # Check if the message buffer contains characters from previous iterations
                parsedData.append([date, time, author, ' '.join(messageBuffer)]) # Save the info from the previous message in parsedData
            messageBuffer.clear() # Clear the message buffer
            # store new message
            date, time, author, message = getDataFields(line)
            messageBuffer.append(message) # Append message to buffer
        else:
            messageBuffer.append(line) # multi-line message.
