class Message:
    message = "Hello World!"
    sender = "Guido van Rossum"

    def __init__(self, message, sender):
        self.message = message
        self.sender = sender

    def to_dict(self):
        return {
            'message': self.message,
            'sender': self.sender
        }  

m = Message('Hi', 'Rob')
print(m.message, m.sender)
print(m.to_dict())
print(m)