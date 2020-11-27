# Whatsapp Chat Analyzer (In progress)
---
Project that is focused on getting information about a whatsapp chat using python libraries such as pandas, matplotlib and seaborn.
---
## Content
1. Requeriments
2. Chat Messages format parsed.
3. Current Functionalities.
4. Future Fucntionalities.
5. Output Examples 

### Requirements

For the current progress just the pandas library is needed. As dataset you could use a whatsapp group chat exporting it from your phone.

### Messages Format

For this analyzer the format of the messages parsed is:
`d/mm/yy, hrs:min am|pm - Auhtor_Name: message...`

As an example:
`4/7/20, 12:44 pm - Jhon Doe: Hey, how are you?`

**Note: the time format is based on the 12 hour system**
### Current Functionallities

* Get Top 3 talkative Authors from a group chat.
* Word and letter count for the total messages in a chat.

### Future Functionalities

* More detailed information of the chat.
* Report generation or graphic interface for the parsed data.

### Output Example

```
-------------REPORT FOR WHATSAPP CHAT-------------

-- TOP 3 MORE TALKATIVE AUTHORS --
The author Jhon Doe writes 7670 messages.
The author Sebastian Torvalds writes 7052 messages.
The author Sr Info writes 5380 messages.

-- WORD AND LETTER COUNT PER MESSAGE INFO --
For the 27842.0 total number of messages, there is an average of 5.28 words and 27.88 letters per message.
```
**Based on: https://towardsdatascience.com/build-your-own-whatsapp-chat-analyzer-9590acca9014**
