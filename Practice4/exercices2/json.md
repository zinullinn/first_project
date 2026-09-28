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

Use `json.load(file)` to read JSON from an open file and `json.dump(value, file, indent=2)` to write it.

## Exercise 1: print interface status

The program in `exercices/json.py` reads `exercices/sample-data.json`. The data contains a top-level `imdata` list. Each list entry has an `l1PhysIf.attributes` object with the distinguished name (`dn`), description (`descr`), speed, and MTU. The program parses those nested attributes and formats them as aligned columns:

```text
Interface Status
=========================================================================================
DN                                                 Description              Speed    MTU
-------------------------------------------------- -------------------- -------- ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150
```

The exercise data includes three sample interfaces. The script processes every item in `imdata`, so it also works with a larger file in the same JSON structure.
