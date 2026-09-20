"""Solutions for the general Python function tasks."""

from itertools import permutations
from math import pi


def grams_to_ounces(grams):
    """Convert grams to ounces."""
    return 28.3495231 * grams


def fahrenheit_to_centigrade(fahrenheit):
    """Convert Fahrenheit to Centigrade."""
    return (5 / 9) * (fahrenheit - 32)


def solve(numheads, numlegs):
    """Return the number of chickens and rabbits, or None if impossible."""
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    if numheads < 0 or numlegs < 0 or numlegs % 2 or rabbits < 0 or chickens < 0:
        return None
    return chickens, rabbits


def is_prime(number):
    """Return True when number is prime."""
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def filter_prime(numbers):
    """Return only prime numbers from a list."""
    return list(filter(lambda number: is_prime(number), numbers))


def string_permutations(text):
    """Return all unique permutations of text."""
    return ["".join(item) for item in sorted(set(permutations(text)))]


def reverse_sentence(sentence):
    """Return a sentence with its words reversed."""
    return " ".join(sentence.split()[::-1])


def has_33(nums):
    """Return True if two 3 values are next to each other."""
    return any(nums[index:index + 2] == [3, 3] for index in range(len(nums) - 1))


def spy_game(nums):
    """Return True if 0, 0, 7 appear in order."""
    target = [0, 0, 7]
    for number in nums:
        if target and number == target[0]:
            target.pop(0)
    return not target


def sphere_volume(radius):
    """Return the volume of a sphere."""
    return 4 / 3 * pi * radius ** 3


def unique_list(items):
    """Return unique values in their first-seen order without using set."""
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items


def is_palindrome(text):
    """Return True if text reads the same in both directions."""
    cleaned_text = "".join(character.lower() for character in text if character.isalnum())
    return cleaned_text == cleaned_text[::-1]


def histogram(numbers):
    """Print one star line for every number."""
    for number in numbers:
        print("*" * number)


if __name__ == "__main__":
    # Here is a short test of the function solutions.
    print(grams_to_ounces(100))
    print(fahrenheit_to_centigrade(68))
    print(solve(35, 94))
    print(filter_prime([1, 2, 3, 4, 5, 10, 11]))
    print(string_permutations("abc"))
    print(reverse_sentence("We are ready"))
    print(has_33([1, 3, 3]))
    print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    print(sphere_volume(3))
    print(unique_list([1, 2, 2, 3, 1]))
    print(is_palindrome("Never odd or even"))
    histogram([4, 9, 7])
