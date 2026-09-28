"""Built-in math, math module, and random module examples."""

import math
import random


def main() -> None:
    values = [4, -2, 7.6, 3]
    print("min/max:", min(values), max(values))
    print("abs/round:", abs(-8), round(3.14159, 2))
    print("pow:", pow(2, 5))

    print("sqrt(81):", math.sqrt(81))
    print("ceil/floor(4.3):", math.ceil(4.3), math.floor(4.3))
    print("sin(pi/2), cos(0):", math.sin(math.pi / 2), math.cos(0))
    print("pi and e:", math.pi, math.e)

    # Seed the generator so the examples produce repeatable results.
    random.seed(42)
    print("random():", random.random())
    print("randint(1, 10):", random.randint(1, 10))
    print("choice:", random.choice(["apple", "banana", "orange"]))
    cards = ["A", "K", "Q", "J"]
    random.shuffle(cards)
    print("shuffled cards:", cards)


if __name__ == "__main__":
    main()
