# Reuses exercise [8-10]
text_messages = [
    'ok',
    'yes',
    'no',
    'hello',
]

sent_messages = []

def send_messages(text_messages, sent_messages):
    while text_messages:
        msg = text_messages.pop()
        sent_messages.append(msg)
        print(msg)

send_messages(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)
