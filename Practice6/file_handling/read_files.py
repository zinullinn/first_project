"""Create a sample file and demonstrate common read and append operations."""
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "demo_data"
SAMPLE = DATA_DIR / "sample.txt"


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    # w creates the file or replaces its contents; use only this practice sample.
    with SAMPLE.open("w", encoding="utf-8") as file:
        file.write("First sample line\nSecond sample line\nThird sample line\n")

    with SAMPLE.open("r", encoding="utf-8") as file:
        print("read():")
        print(file.read(), end="")
    with SAMPLE.open("r", encoding="utf-8") as file:
        print("\nreadline():")
        print(file.readline(), end="")
    with SAMPLE.open("r", encoding="utf-8") as file:
        print("\nreadlines():")
        print(file.readlines())

    # a appends without replacing existing content.
    with SAMPLE.open("a", encoding="utf-8") as file:
        file.write("Appended line\n")
    print("\nAfter appending:")
    print(SAMPLE.read_text(encoding="utf-8"), end="")

    # x creates only if the file does not already exist.
    exclusive_sample = DATA_DIR / "exclusive.txt"
    try:
        with exclusive_sample.open("x", encoding="utf-8") as file:
            file.write("Created with x mode\n")
        print(f"Created {exclusive_sample.name} with x mode.")
    except FileExistsError:
        print(f"{exclusive_sample.name} already exists; x mode did not overwrite it.")


if __name__ == "__main__":
    main()
