"""Examples of functions that return useful values."""


def get_rectangle_details(width, height):
    """Return the area and perimeter of a rectangle."""
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


# Here is unpacking of two returned values.
rectangle_area, rectangle_perimeter = get_rectangle_details(8, 5)
print(f"Area: {rectangle_area}")
print(f"Perimeter: {rectangle_perimeter}")
