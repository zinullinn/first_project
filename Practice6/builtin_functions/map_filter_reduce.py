"""Examples of common built-ins and functools.reduce."""
from functools import reduce


def main():
    values = [3, 8, 2, 5, 10]
    print("len:", len(values), "sum:", sum(values))
    print("min/max:", min(values), max(values))
    print("map (squares):", list(map(lambda n: n * n, values)))
    print("filter (even):", list(filter(lambda n: n % 2 == 0, values)))
    print("reduce (product):", reduce(lambda total, n: total * n, values, 1))
    print("sorted:", sorted(values), "descending:", sorted(values, reverse=True))

    number_text = "42"
    decimal_text = "3.5"
    print("type:", type(number_text))
    print("isinstance:", isinstance(int(number_text), int))
    print("Conversions:", int(number_text), float(decimal_text), str(42), bool(1))


if __name__ == "__main__":
    main()
