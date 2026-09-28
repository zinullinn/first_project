"""JSON parsing, serialization, and file operations for Practice 4."""

import sys
from pathlib import Path

# This required exercise filename matches the standard-library module. Temporarily
# remove its directory from the import search path so `import json` finds the library.
exercise_directory = str(Path(__file__).resolve().parent)
removed_paths = [path for path in sys.path if str(Path(path or ".").resolve()) == exercise_directory]
sys.path[:] = [path for path in sys.path if str(Path(path or ".").resolve()) != exercise_directory]
import json
sys.path[:0] = removed_paths

DATA_FILE = Path(__file__).with_name("sample-data.json")


def main() -> None:
    # JSON text to Python objects with json.loads().
    json_text = '{"name": "Aida", "score": 92, "passed": true}'
    student = json.loads(json_text)
    print("parsed JSON:", student)

    # Python objects to JSON text with json.dumps().
    new_student = {"name": "Timur", "score": 88, "passed": True}
    print("serialized JSON:", json.dumps(new_student, indent=2))

    # Read the provided sample and work with its nested list of records.
    with DATA_FILE.open("r", encoding="utf-8") as file:
        course_data = json.load(file)
    active_students = [item["name"] for item in course_data["students"] if item["active"]]
    average_score = sum(item["score"] for item in course_data["students"]) / len(course_data["students"])
    print("course:", course_data["course"])
    print("active students:", active_students)
    print("average score:", round(average_score, 2))

    # Write a separate output file next to this exercise, leaving sample-data.json intact.
    output_file = DATA_FILE.with_name("output.json")
    with output_file.open("w", encoding="utf-8") as file:
        json.dump({"active_students": active_students, "average_score": average_score}, file, indent=2)
    print("wrote:", output_file.name)


if __name__ == "__main__":
    main()
