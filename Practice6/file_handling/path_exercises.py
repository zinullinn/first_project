"""Line count, alphabet file generation, copy, and guarded path deletion."""
from pathlib import Path
import shutil
import string
import sys

DATA_DIR = Path(__file__).resolve().parents[1] / "demo_data" / "path_exercises"


def count_lines(path: Path) -> int:
    with Path(path).open("r", encoding="utf-8") as file:
        return sum(1 for _ in file)


def write_list_to_file(values, path: Path) -> None:
    with Path(path).open("w", encoding="utf-8") as file:
        for value in values:
            file.write(f"{value}\n")


def generate_letter_files(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for letter in string.ascii_uppercase:
        (directory / f"{letter}.txt").write_text(f"File for {letter}\n", encoding="utf-8")


def copy_file(source: Path, destination: Path) -> None:
    if not Path(source).is_file():
        raise FileNotFoundError(f"Source file does not exist: {source}")
    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def delete_specified_file(path: Path) -> bool:
    """Guarded helper for an explicit path; caller must supply the intended file."""
    path = Path(path)
    if not path.exists():
        print(f"Path does not exist: {path}")
        return False
    if not path.is_file():
        print(f"Path is not a file: {path}")
        return False
    if not path.stat().st_mode & 0o222 or not path.parent.stat().st_mode & 0o222:
        print(f"No write access to file or parent directory: {path}")
        return False
    path.unlink()
    print(f"Deleted: {path}")
    return True


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    sample = DATA_DIR / "count_me.txt"
    write_list_to_file(["one", "two", "three"], sample)
    print(f"Line count in {sample.name}: {count_lines(sample)}")

    letters = DATA_DIR / "letters"
    generate_letter_files(letters)
    print(f"Generated {len(list(letters.glob('*.txt')))} files from A.txt to Z.txt")

    copied = DATA_DIR / "count_me_copy.txt"
    copy_file(sample, copied)
    print(f"Copied contents to {copied.name}: {copied.read_text(encoding='utf-8')!r}")

    # Demonstrate deletion safely on a newly created disposable file.
    disposable = DATA_DIR / "disposable.txt"
    disposable.write_text("Temporary practice file\n", encoding="utf-8")
    delete_specified_file(disposable)

    if len(sys.argv) > 1:
        requested = Path(sys.argv[1]).expanduser()
        print("Requested path exists:", requested.exists())
        if requested.exists():
            print("Directory portion:", requested.parent)
            print("Filename portion:", requested.name)
        print("To practice the guarded deletion helper, edit this script to call")
        print("delete_specified_file(requested) after confirming the intended path.")


if __name__ == "__main__":
    main()
