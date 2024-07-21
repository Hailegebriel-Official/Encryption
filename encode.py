# this code used to encode any text message
# for leaning purpose
# powerd by mosa technologies 
# its end to end encrypted 
message = str(input('input the message for encryption : '))
encoded_message = ''
for words in message:
    words = words.lower()
    if words == 'z':
        words = '`'
    encoding = ord(words) + 1
    encoded_message += chr(encoding)

print(encoded_message)

