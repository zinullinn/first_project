"""Find lowercase-word sequences joined by underscores."""

import re


def find_underscore_sequences(text: str) -> list[str]:
    return re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", text)


if __name__ == "__main__":
    print(find_underscore_sequences("good_day use snake_case and bad_Name"))
