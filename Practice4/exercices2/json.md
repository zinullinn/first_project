# JSON

JSON (JavaScript Object Notation) stores structured data as objects, arrays, strings, numbers, booleans, and `null`.

```python
import json

text = '{"name": "Aida", "score": 92, "active": true}'
student = json.loads(text)              # JSON text -> Python dict
print(student["name"], student["score"])

encoded = json.dumps(student, indent=2) # Python value -> JSON text
print(encoded)
```

Use `json.load(file)` to read JSON from an open file and `json.dump(value, file, indent=2)` to write it. The companion `exercices/json.py` reads `sample-data.json`, selects active students, calculates the average score, and writes a JSON result file.
