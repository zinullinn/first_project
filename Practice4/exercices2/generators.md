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
