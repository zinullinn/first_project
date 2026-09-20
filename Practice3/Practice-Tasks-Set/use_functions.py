"""Import and use functions from the LAB 3 solutions."""

from functions_tasks import filter_prime, grams_to_ounces, reverse_sentence, sphere_volume


def main():
    """Show functions imported from functions_tasks."""
    # Here is an import example using four earlier functions.
    print(grams_to_ounces(250))
    print(filter_prime([2, 4, 5, 8, 11]))
    print(reverse_sentence("Python functions are useful"))
    print(round(sphere_volume(2), 2))


if __name__ == "__main__":
    main()
