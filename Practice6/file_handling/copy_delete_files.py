"""Copy/backup examples and a guarded delete of a disposable practice file."""
from pathlib import Path
import shutil

DATA_DIR = Path(__file__).resolve().parents[1] / "demo_data"


def delete_file_safely(path: Path) -> bool:
    """Delete an existing writable regular file; report why it was skipped."""
    path = Path(path)
    if not path.exists():
        print(f"Not deleting: {path} does not exist.")
        return False
    if not path.is_file():
        print(f"Not deleting: {path} is not a regular file.")
        return False
    if not path.stat().st_mode & 0o222:
        print(f"Not deleting: {path} has no write permission bits.")
        return False
    if not path.parent.exists() or not path.parent.stat().st_mode & 0o222:
        print(f"Not deleting: parent folder is not writable: {path.parent}")
        return False
    path.unlink()
    print(f"Deleted {path}")
    return True


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    source = DATA_DIR / "copy_source.txt"
    source.write_text("A small file for copy and backup practice.\n", encoding="utf-8")
    copy = DATA_DIR / "copy_result.txt"
    backup = DATA_DIR / "copy_source.bak"
    shutil.copy2(source, copy)
    shutil.copy2(source, backup)
    print(f"Copied to {copy.name} and backed up to {backup.name}.")

    disposable = DATA_DIR / "delete_me.txt"
    disposable.write_text("Disposable sample file.\n", encoding="utf-8")
    delete_file_safely(disposable)


if __name__ == "__main__":
    main()
