# File handling demo

This workspace contains a small Python demo that illustrates:

- Reading and writing text files and CSVs
- Automating file operations: rename, move, delete
- Using try/except to handle errors safely

Files:

- `file_utils.py`: utilities and `demo_operations()` function
- `run_demo.py`: runs the demo and prints outputs

Quick run:

```bash
python run_demo.py
```

Sample output files are written to the `samples/` directory. To create sample
screenshots, open the generated files (e.g., `samples/output.txt`) in a text
editor and capture your screen using your OS screenshot tool.

## Tests

Run the unit tests with Python's unittest discovery:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

After running tests, a copy of the last test run output is saved at
`tests/test_results.txt`.

If you want example screenshots of the outputs, open `samples/output.txt` and
`tests/test_results.txt` in an editor and capture your screen (Windows: Win+Shift+S).

