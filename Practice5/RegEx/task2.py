"""Match a string containing 'a' followed by two or three 'b' characters."""

import re


def matches_a_then_two_or_three_b(text: str) -> bool:
    return re.fullmatch(r"ab{2,3}", text) is not None


if __name__ == "__main__":
    for sample in ("abb", "abbb", "ab", "abbbb"):
        print(f"{sample!r}: {matches_a_then_two_or_three_b(sample)}")
