"""Parse sample-data.json and display physical interface status."""

import sys
from pathlib import Path

# This required exercise filename matches the standard-library module. Temporarily
# remove its directory from the import path so `import json` finds the library.
exercise_directory = str(Path(__file__).resolve().parent)
removed_paths = [path for path in sys.path if str(Path(path or ".").resolve()) == exercise_directory]
sys.path[:] = [path for path in sys.path if str(Path(path or ".").resolve()) != exercise_directory]
import json
sys.path[:0] = removed_paths

DATA_FILE = Path(__file__).with_name("sample-data.json")
DN_WIDTH = 50
DESCRIPTION_WIDTH = 20
SPEED_WIDTH = 8
MTU_WIDTH = 6


def main() -> None:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    heading = (
        f"{'DN':<{DN_WIDTH}} "
        f"{'Description':<{DESCRIPTION_WIDTH}} "
        f"{'Speed':>{SPEED_WIDTH}} "
        f"{'MTU':>{MTU_WIDTH}}"
    )
    print("Interface Status")
    print("=" * len(heading))
    print(heading)
    print(
        f"{'-' * DN_WIDTH} "
        f"{'-' * DESCRIPTION_WIDTH} "
        f"{'-' * SPEED_WIDTH} "
        f"{'-' * MTU_WIDTH}"
    )

    for item in data.get("imdata", []):
        attributes = item.get("l1PhysIf", {}).get("attributes", {})
        print(
            f"{attributes.get('dn', ''):<{DN_WIDTH}} "
            f"{attributes.get('descr', ''):<{DESCRIPTION_WIDTH}} "
            f"{attributes.get('speed', ''):>{SPEED_WIDTH}} "
            f"{attributes.get('mtu', ''):>{MTU_WIDTH}}"
        )


if __name__ == "__main__":
    main()
