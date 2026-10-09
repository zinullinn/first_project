"""Create nested sample folders and practice listing/path checks."""
from pathlib import Path
import os

DATA_DIR = Path(__file__).resolve().parents[1] / "demo_data"


def list_path(path: Path) -> None:
    """Print directories only, files only, and all immediate entries."""
    path = Path(path)
    if not path.exists() or not path.is_dir():
        print(f"Not an existing directory: {path}")
        return
    entries = list(path.iterdir())
    print("Directories:", [entry.name for entry in entries if entry.is_dir()])
    print("Files:", [entry.name for entry in entries if entry.is_file()])
    print("All entries:", [entry.name for entry in entries])


def main():
    nested = DATA_DIR / "nested" / "level_two"
    nested.mkdir(parents=True, exist_ok=True)  # like os.makedirs(..., exist_ok=True)
    (DATA_DIR / "notes.txt").write_text("Example note\n", encoding="utf-8")
    (DATA_DIR / "image.png").write_bytes(b"sample")
    (nested / "inside.txt").write_text("Nested example\n", encoding="utf-8")

    print("Working directory:", os.getcwd())
    print("Names from os.listdir:", os.listdir(DATA_DIR))
    list_path(DATA_DIR)
    print("Text files:", [p.name for p in DATA_DIR.rglob("*.txt") if p.is_file()])

    target = DATA_DIR / "notes.txt"
    print("Path exists/readable/writable/executable:",
          os.path.exists(target), os.access(target, os.R_OK),
          os.access(target, os.W_OK), os.access(target, os.X_OK))
    if target.exists():
        print("Path:", target)
        print("Parent directory:", target.parent)
        print("Filename:", target.name)
    print("Exists with pathlib:", target.exists())

    # os.mkdir makes one level; os.rmdir removes an empty directory.
    single = DATA_DIR / "single_level"
    if not single.exists():
        os.mkdir(single)
    os.rmdir(single)
    print("Created then removed empty directory:", single.name)

    # os.chdir changes process-wide state, so demonstrate and immediately restore it.
    old_cwd = Path.cwd()
    try:
        os.chdir(DATA_DIR)
        print("Temporary os.chdir/getcwd demo:", os.getcwd())
    finally:
        os.chdir(old_cwd)


if __name__ == "__main__":
    main()
