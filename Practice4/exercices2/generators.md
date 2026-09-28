# Iterators and generators

An iterator returns values one at a time. `iter()` obtains an iterator and `next()` requests its next value; iteration ends with `StopIteration`.

```python
numbers = iter([10, 20, 30])
print(next(numbers))
for number in numbers:
    print(number)
```

A custom iterator implements `__iter__()` and `__next__()`. A generator function uses `yield` to produce values lazily:

```python
def even_numbers(limit):
    number = 0
    while number < limit:
        yield number
        number += 2
```

Generator expressions provide a concise lazy alternative, for example `(n * n for n in range(5))`. They can process large sequences without building a complete list in memory.

## Exercises

The following examples use inclusive endpoints where the prompt says "up to" or "between."

```python
def square_numbers(n):
    for number in range(n + 1):
        yield number**2


def even_numbers(n):
    # Print each value separated by a comma without building a list.
    first = True
    for number in range(0, n + 1, 2):
        if not first:
            print(",", end="")
        print(number, end="")
        first = False
    print()


def divisible_by_3_and_4(n):
    for number in range(n + 1):
        if number % 3 == 0 and number % 4 == 0:
            yield number


def squares(a, b):
    for number in range(a, b + 1):
        yield number**2


def countdown(n):
    while n >= 0:
        yield n
        n -= 1


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print("Squares from 0 through n:", list(square_numbers(n)))
    print("Even numbers:", end=" ")
    even_numbers(n)
    print("Divisible by both 3 and 4:", list(divisible_by_3_and_4(n)))

    a = int(input("Enter a: "))
    b = int(input("Enter b (at least a): "))
    if b < a:
        raise ValueError("b must be greater than or equal to a")
    print(f"Squares from {a} through {b}:")
    for value in squares(a, b):
        print(value)

    print("Countdown:", list(countdown(n)))
```
