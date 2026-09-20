"""One class can inherit features from more than one parent."""


class Camera:
    """Provide a camera feature."""

    def take_photo(self):
        return "Photo taken."


class Phone:
    """Provide a phone feature."""

    def make_call(self):
        return "Calling a contact."


class SmartPhone(Camera, Phone):
    """Combine camera and phone features."""


# Here is multiple inheritance in one object.
device = SmartPhone()
print(device.take_photo())
print(device.make_call())
