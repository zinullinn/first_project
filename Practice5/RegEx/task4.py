"""Find a capital letter followed by one or more lowercase letters."""

import re


def find_capitalized_words(text: str) -> list[str]:
    return re.findall(r"\b[A-Z][a-z]+\b", text)


if __name__ == "__main__":
    print(find_capitalized_words("Alice met BOB and Charlie in NewYork."))
