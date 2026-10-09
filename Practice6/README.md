# Practice 6: Python File Handling and Built-in Functions

Examples for practicing file operations, directory management, and common Python built-ins. They use `pathlib` and create their demonstration files under `Practice6/demo_data/` when run, so they do not modify files outside this practice folder.

## W3Schools topics

Study [Python File Handling](https://www.w3schools.com/python/python_file_handling.asp), including modes `r`, `w`, `a`, and `x`; `read()`, `readline()`, and `readlines()`; writing and appending; and context managers (`with`). Also review `os`, `shutil`, `pathlib`, directory operations (`mkdir`, `makedirs`, `listdir`, `chdir`, `getcwd`, `rmdir`), and the built-ins demonstrated below.

## Examples

- `file_handling/read_files.py`: create a sample text file, read it with the three read methods, append lines, and verify.
- `file_handling/write_files.py`: write a list of values using a context manager.
- `file_handling/copy_delete_files.py`: copy and back up files; demonstrate safe deletion after checking existence and write access. The deletion example targets only a disposable file it creates itself.
- `directory_management/create_list_dirs.py`: create nested folders, list directory contents, filter by extension, check path access/existence, and show filename/parent path. Includes listing directories only, files only, and all entries for a specified path.
- `directory_management/move_files.py`: copy and move a sample file between practice data folders with `shutil`.
- `builtin_functions/map_filter_reduce.py`: `len`, `sum`, `min`, `max`, `map`, `filter`, `reduce`, `sorted`, `type`, and type conversions.
- `builtin_functions/enumerate_zip_examples.py`: paired iteration with `enumerate` and `zip`.
- `file_handling/path_exercises.py`: count lines, generate A.txt through Z.txt, copy a file, and safely delete a specified path after access checks.

Run an example from the repository root, for example:

```powershell
python Practice6/file_handling/read_files.py
```

The path exercise accepts an optional filename for the line-count/copy demonstration. Destructive deletion is limited to the disposable sample file created by that script; the general delete helper is provided as an exercise and requires an explicit existing file path.
