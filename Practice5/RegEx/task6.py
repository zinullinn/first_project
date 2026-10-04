"""Replace each space, comma, or dot with a colon."""

import re


def replace_separators(text: str) -> str:
    return re.sub(r"[ ,.]", ":", text)


if __name__ == "__main__":
    print(replace_separators("Hello, world. Regex is useful"))
