"""Examples of *args and **kwargs."""


def describe_order(*items, **details):
    """Build a message from any number of items and named details."""
    item_list = ", ".join(items)
    customer = details.get("customer", "Guest")
    delivery = details.get("delivery", "standard")
    return f"{customer} ordered: {item_list}. Delivery: {delivery}."


# Here is a call with flexible positional and keyword arguments.
print(describe_order("tea", "bread", customer="Dana", delivery="express"))
