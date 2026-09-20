"""A child class can replace a parent method."""


class Notification:
    """Represent a general notification."""

    def send(self):
        return "Sending a notification."


class EmailNotification(Notification):
    """Represent an email notification."""

    def send(self):
        return "Sending an email notification."


# Here is an overridden method called on a child object.
message = EmailNotification()
print(message.send())
