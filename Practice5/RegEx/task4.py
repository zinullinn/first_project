"""Splitting text and replacing patterns."""

import re


def main() -> None:
    print("split on commas/semicolons:", re.split(r"[,;]\s*", "apples, pears; plums"))
    print("replace digits:", re.sub(r"\d+", "#", "Room 12, floor 3"))
    print("limit replacements:", re.sub(r"\s+", " ", "extra    spaces   here", count=1))


if __name__ == "__main__":
    main()
