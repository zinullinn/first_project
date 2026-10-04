"""First match, all matches, and match-at-start examples."""

import re


def main() -> None:
    text = "Order A-104: 3 items, order B-208: 5 items"
    print("search:", re.search(r"[A-Z]-\d+", text).group())
    print("findall:", re.findall(r"\d+", text))
    print("match at beginning:", re.match(r"Order", text).group())
    print("match away from beginning:", re.match(r"A-104", text))


if __name__ == "__main__":
    main()
