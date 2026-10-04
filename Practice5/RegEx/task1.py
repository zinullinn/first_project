"""Match a string containing 'a' followed by zero or more 'b' characters."""

import re


def matches_a_then_zero_or_more_b(text: str) -> bool:
    return re.fullmatch(r"ab*", text) is not None


if __name__ == "__main__":
    for sample in ("a", "ab", "abbb", "ac", "ba"):
        print(f"{sample!r}: {matches_a_then_zero_or_more_b(sample)}")
