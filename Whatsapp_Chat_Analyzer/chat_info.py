"""Get information about the whatsapp chat"""

from data_frame import newDataFrame


data_frame = newDataFrame()

messages_per_author = dict(data_frame['Author'].value_counts())
print('-------------REPORT FOR WHATSAPP CHAT-------------')
print()

print('-- TOP 3 MORE TALKATIVE AUTHORS --')
for author, messages in sorted(messages_per_author.items(), key=lambda item: item[1], reverse=True)[:3]:
    print('The author ' + author.strip() + ' writes ' + str(messages) + ' messages.')

print()
print('-- WORD AND LETTER COUNT PER MESSAGE INFO --')

data_frame['Word_Count'] = data_frame['Message'].apply(lambda s: len(s.split(' ')))
data_frame['Letter_Count'] = data_frame['Message'].apply(lambda s: len(s))

words_info = dict(data_frame['Word_Count'].describe())
letter_info = dict(data_frame['Letter_Count'].describe())

print("For the " + str(words_info['count']) + " total number of messages, there is an average of " + str(round(words_info['mean'], 2)) + " words and " + str(round(letter_info['mean'], 2)) + " letters per message.")
