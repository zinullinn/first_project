"""Iterator and generator examples for Practice 4."""


class CountUp:
    """An iterator yielding integers from start through stop, inclusive."""

    def __init__(self, start: int, stop: int) -> None:
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


def even_numbers(limit: int):
    """Yield even numbers from zero up to (but not including) limit."""
    number = 0
    while number < limit:
        yield number
        number += 2


def main() -> None:
    # iter() creates an iterator; next() advances it one item at a time.
    colors = iter(["red", "green", "blue"])
    print("next():", next(colors))
    print("remaining iterator items:", list(colors))

    print("custom iterator:", list(CountUp(1, 5)))
    print("loop through iterator:", end=" ")
    for value in CountUp(3, 6):
        print(value, end=" ")
    print()

    print("generator function:", list(even_numbers(10)))
    squares = (number * number for number in range(1, 6))
    print("generator expression:", list(squares))


if __name__ == "__main__":
    main()
