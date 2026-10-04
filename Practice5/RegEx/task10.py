"""Convert camelCase or PascalCase text to snake_case."""

import re


def camel_to_snake(text: str) -> str:
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", text)
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return text.lower()


if __name__ == "__main__":
    print(camel_to_snake("camelCase"))
    print(camel_to_snake("XMLHttpRequest"))
