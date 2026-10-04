"""Special sequences and bounded quantifiers."""

import re


def main() -> None:
    text = "User_7 emailed user@example.com on 2025-03-08.\nCall: 555-1234"
    for pattern in (r"\d+", r"\w+", r"\s+", r"\D+", r"\W+", r"\S+"):
        print(f"{pattern}: {re.findall(pattern, text)[:5]}")
    print(r"\A beginning:", bool(re.search(r"\AUser", text)))
    print(r"\Z ending:", bool(re.search(r"1234\Z", text)))
    print("exactly four digits:", re.findall(r"\d{4}", text))
    print("at least two digits:", re.findall(r"\d{2,}", text))
    print("two to four digits:", re.findall(r"\d{2,4}", text))
    print("email-like:", re.findall(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text))


if __name__ == "__main__":
    main()
