class Email:
    def __init__(self, sender, reciver, content):
        self.sender = sender
        self.receiver = reciver
        self.content = content
        self.is_sent = False
    def sent(self):
        self.is_sent = True
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
emails = []

info_mail = input().split()
while "Stop" not in info_mail:
    sender = info_mail[0]
    reciver = info_mail[1]
    content = info_mail[2]
    email = Email(sender, reciver, content)
    emails.append(email)
    print(emails)
    info_mail = input()

