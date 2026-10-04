"""Split a string immediately before each uppercase letter."""

import re


def split_at_uppercase(text: str) -> list[str]:
    return [part for part in re.split(r"(?=[A-Z])", text) if part]


if __name__ == "__main__":
    print(split_at_uppercase("SplitAtCapitalLetters"))
