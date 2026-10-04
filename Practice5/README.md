# Practice 5: Python Regular Expressions

Runnable examples for Python's `re` module, plus a receipt parser. These examples cover regex syntax, metacharacters, special sequences, character classes, quantifiers, flags, and `search`, `findall`, `split`, `sub`, and `match`.

## Files

- `receipt_parser.py` parses the included `raw.txt` receipt into JSON.
- `raw.txt` is a sample receipt used by the parser. No receipt file was present in the repository when this practice was created.
- `RegEx/task1.py` demonstrates metacharacters and character classes.
- `RegEx/task2.py` demonstrates special sequences and quantifiers.
- `RegEx/task3.py` demonstrates `search`, `findall`, and `match`.
- `RegEx/task4.py` demonstrates `split` and `sub`.
- `RegEx/task5.py` demonstrates regex flags.

Run from the repository root:

```powershell
python Practice5/receipt_parser.py
python Practice5/RegEx/task1.py
python Practice5/RegEx/task2.py
python Practice5/RegEx/task3.py
python Practice5/RegEx/task4.py
python Practice5/RegEx/task5.py
```

The receipt parser reads its input from the same directory as the script. It handles common currency symbols, optional thousands separators, multiple date/time styles, and payment labels. When the provided course `raw.txt` or `regex.md` becomes available, replace the sample receipt or adapt the practice inputs as needed.

## W3Schools study checklist

Use the [W3Schools Python RegEx tutorial](https://www.w3schools.com/python/python_regex.asp) to read each section and complete its interactive exercises. The scripts here provide runnable examples for the listed topics; they do not record completion of the website's interactive exercises.
