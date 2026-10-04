"""Regex syntax, metacharacters, alternation, groups, and character classes."""

import re


def main() -> None:
    text = "cat cot cut cart dog"
    print("dot + quantifier:", re.findall(r"c.t", text))       # . matches any character
    print("zero or more:", re.findall(r"ca*t", "ct cat caat"))
    print("one or more:", re.findall(r"ca+t", "ct cat caat"))
    print("optional:", re.findall(r"colou?r", "color colour"))
    print("start/end:", bool(re.search(r"^cat", text)), bool(re.search(r"dog$", text)))
    print("set/range:", re.findall(r"c[ao]t", text), re.findall(r"[a-z]+", text))
    print("negated set:", re.findall(r"[^ ]+", "red blue"))
    print("alternation:", re.findall(r"cat|dog", text))
    print("group:", re.findall(r"(ca)(t)", "cat"))
    print("escaped dot:", re.findall(r"\.", "a.b"))


if __name__ == "__main__":
    main()
