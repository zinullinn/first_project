# Math and random

Python includes built-in numeric helpers and the `math` and `random` modules.

```python
import math
import random

print(min(3, 8), max(3, 8), abs(-4), round(3.14159, 2))
print(pow(2, 5), math.sqrt(81), math.ceil(4.2), math.floor(4.8))
print(math.sin(math.pi / 2), math.cos(0), math.e)

print(random.random())             # float in [0.0, 1.0)
print(random.randint(1, 6))        # integer including both endpoints
print(random.choice(["A", "B"]))
cards = ["A", "K", "Q"]
random.shuffle(cards)              # shuffles the list in place
```

Use `random.seed(value)` when a repeatable sequence is useful for demonstrations. For security-sensitive random values, use Python's `secrets` module instead.
