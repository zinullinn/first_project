"""Regex flags for case-insensitive, multiline, and dot-all matching."""

import re


def main() -> None:
    text = "First line\nsecond LINE\nlast line"
    print("IGNORECASE:", re.findall(r"line", text, re.IGNORECASE))
    print("MULTILINE anchors:", re.findall(r"^.*line$", text, re.IGNORECASE | re.MULTILINE))
    print("DOTALL:", bool(re.search(r"First.*last", text, re.DOTALL)))


if __name__ == "__main__":
    main()
