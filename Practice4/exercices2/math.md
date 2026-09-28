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

## Geometry and angle exercises

```python
import math


def degrees_to_radians(degrees):
    return math.radians(degrees)


def trapezoid_area(height, first_base, second_base):
    return (first_base + second_base) * height / 2


def regular_polygon_area(number_of_sides, side_length):
    if number_of_sides < 3:
        raise ValueError("A polygon must have at least 3 sides")
    return number_of_sides * side_length**2 / (4 * math.tan(math.pi / number_of_sides))


def parallelogram_area(base, height):
    return base * height


if __name__ == "__main__":
    degrees = float(input("Input degree: "))
    print("Output radian:", f"{degrees_to_radians(degrees):.6f}")

    height = float(input("Height: "))
    first_base = float(input("Base, first value: "))
    second_base = float(input("Base, second value: "))
    print("Trapezoid area:", trapezoid_area(height, first_base, second_base))

    sides = int(input("Input number of sides: "))
    side_length = float(input("Input the length of a side: "))
    print("The area of the polygon is:", round(regular_polygon_area(sides, side_length)))

    base = float(input("Length of base: "))
    parallelogram_height = float(input("Height of parallelogram: "))
    print("Parallelogram area:", float(parallelogram_area(base, parallelogram_height)))
```

For 15 degrees, the standard conversion is `15 * pi / 180 = 0.261799` radians (approximately); the sample value `0.261904` in the prompt is slightly inaccurate. The regular-polygon formula gives 625 for a square with side length 25.
