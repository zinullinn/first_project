"""Insert spaces at boundaries before capitalized words."""

import re


def add_spaces_before_capitals(text: str) -> str:
    # Also keep acronym runs together: XMLHttpRequest -> XML Http Request.
    text = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", text)
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", text)


if __name__ == "__main__":
    print(add_spaces_before_capitals("HelloWorld and XMLHttpRequest"))
