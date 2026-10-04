"""Convert snake_case text to camelCase."""

import re


def snake_to_camel(text: str) -> str:
    return re.sub(r"_([a-zA-Z0-9])", lambda match: match.group(1).upper(), text)


if __name__ == "__main__":
    print(snake_to_camel("this_is_snake_case"))
