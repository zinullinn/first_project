"""Match text beginning with 'a' and ending with 'b'."""

import re


def starts_with_a_ends_with_b(text: str) -> bool:
    return re.fullmatch(r"a.*b", text, flags=re.DOTALL) is not None


if __name__ == "__main__":
    for sample in ("ab", "a123b", "a line\nand b", "ba"):
        print(f"{sample!r}: {starts_with_a_ends_with_b(sample)}")
