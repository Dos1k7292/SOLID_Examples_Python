from abc import ABC, abstractmethod

class IMessageSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailSender(IMessageSender):
    def send(self, message: str):
        print(f"Email sent: {message}")

class SmsSender(IMessageSender):
    def send(self, message: str):
        print(f"SMS sent: {message}")

class NotificationService:
    def __init__(self, senders: list[IMessageSender]):
        self.senders = senders

    def send_notification(self, message: str):
        for sender in self.senders:
            sender.send(message)

if __name__ == "__main__":
    service = NotificationService([EmailSender(), SmsSender()])
    service.send_notification("Hello, SOLID!")
