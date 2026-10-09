"""Write a list of strings to a text file using a context manager."""
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "demo_data"
OUTPUT = DATA_DIR / "list_output.txt"


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    items = ["apples", "bananas", "cherries"]
    with OUTPUT.open("w", encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")
    print(f"Wrote {len(items)} items to {OUTPUT}")
    print(OUTPUT.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
