"""Copy and move sample files between directories with shutil."""
from pathlib import Path
import shutil

DATA_DIR = Path(__file__).resolve().parents[1] / "demo_data"


def main():
    incoming = DATA_DIR / "incoming"
    organized = DATA_DIR / "organized"
    incoming.mkdir(parents=True, exist_ok=True)
    organized.mkdir(parents=True, exist_ok=True)

    source = incoming / "report.txt"
    source.write_text("Practice file movement.\n", encoding="utf-8")
    copied = organized / "report_copy.txt"
    shutil.copy2(source, copied)
    print(f"Copied {source.name} to {copied}")

    moved = organized / "report_moved.txt"
    shutil.move(str(source), str(moved))
    print(f"Moved {source.name} to {moved}")


if __name__ == "__main__":
    main()
