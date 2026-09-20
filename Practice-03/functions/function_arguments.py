"""Examples of positional and default function arguments."""


def calculate_ticket_price(age, is_student=False):
    """Return a simple ticket price based on age and student status."""
    if age < 12:
        return 0
    if is_student:
        return 1500
    return 2500


# Here is a call using positional and default arguments.
print(calculate_ticket_price(10))
print(calculate_ticket_price(19, True))
