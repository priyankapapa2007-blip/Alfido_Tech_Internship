import os
import shutil
import csv
import traceback

"""
file_utils.py

Demonstrates basic file handling, automation (rename/move/delete),
and exception handling using try/except. The functions are small and
documented so you can reuse them in scripts or expand them.

Run `python run_demo.py` to see a demonstration that creates sample
inputs, performs file operations, and writes outputs.
"""


def read_text(path):
    """Read a text file and return its contents as a string.

    Uses try/except to catch IO errors and returns None on failure.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        print(f"Error reading text file: {path}")
        traceback.print_exc()
        return None


def write_text(path, text):
    """Write `text` to `path`, creating parent directories if needed."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True
    except Exception:
        print(f"Error writing text file: {path}")
        traceback.print_exc()
        return False


def append_text(path, text):
    """Append `text` to a file (creates it if missing)."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'a', encoding='utf-8') as f:
            f.write(text)
        return True
    except Exception:
        print(f"Error appending to text file: {path}")
        traceback.print_exc()
        return False


def read_csv(path):
    """Read a CSV file and return a list of rows (each row is a list)."""
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]
    except Exception:
        print(f"Error reading CSV file: {path}")
        traceback.print_exc()
        return None


def write_csv(path, rows):
    """Write rows (iterable of iterables) to a CSV file."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)
        return True
    except Exception:
        print(f"Error writing CSV file: {path}")
        traceback.print_exc()
        return False


def move_file(src, dst):
    """Move file from src to dst. Creates destination directory if needed."""
    try:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
        return True
    except Exception:
        print(f"Error moving file {src} -> {dst}")
        traceback.print_exc()
        return False


def rename_file(src, new_name):
    """Rename a file to `new_name` in the same directory.

    Returns the new absolute path on success, else None.
    """
    try:
        dirpath = os.path.dirname(src)
        dst = os.path.join(dirpath, new_name)
        os.rename(src, dst)
        return dst
    except Exception:
        print(f"Error renaming file {src} -> {new_name}")
        traceback.print_exc()
        return None


def delete_file(path):
    """Delete a file if it exists. Uses safe exception handling."""
    try:
        if os.path.exists(path):
            os.remove(path)
            return True
        else:
            print(f"File does not exist, nothing to delete: {path}")
            return False
    except Exception:
        print(f"Error deleting file: {path}")
        traceback.print_exc()
        return False


def demo_operations(base_dir='samples'):
    """A demonstration sequence that creates sample inputs and exercises
    read/write, rename, move, and delete operations while capturing
    outputs in an output file.
    """
    # Ensure base_dir is a directory under current working dir
    base_dir = os.path.abspath(base_dir)
    os.makedirs(base_dir, exist_ok=True)

    txt_in = os.path.join(base_dir, 'input.txt')
    csv_in = os.path.join(base_dir, 'input.csv')
    txt_out = os.path.join(base_dir, 'output.txt')
    csv_out = os.path.join(base_dir, 'output.csv')

    # Create sample inputs (overwrite if present)
    write_text(txt_in, 'Hello world\nThis is sample text.\n')
    write_csv(csv_in, [['name', 'age'], ['Alice', '30'], ['Bob', '25']])

    # Capture operations log
    log_lines = []

    # Read files
    txt = read_text(txt_in)
    if txt is not None:
        log_lines.append('Read text file successfully')
        log_lines.append(txt)
    else:
        log_lines.append('Failed to read text file')

    rows = read_csv(csv_in)
    if rows is not None:
        log_lines.append('Read CSV file successfully')
        log_lines.append(str(rows))
    else:
        log_lines.append('Failed to read CSV file')

    # Rename text file
    renamed = rename_file(txt_in, 'input_renamed.txt')
    if renamed:
        log_lines.append(f'Renamed text file to {os.path.basename(renamed)}')
        txt_in = renamed
    else:
        log_lines.append('Rename failed')

    # Move CSV to a subfolder
    moved = move_file(csv_in, os.path.join(base_dir, 'archived', 'input.csv'))
    if moved:
        log_lines.append('Moved CSV into archived folder')
        csv_in = os.path.join(base_dir, 'archived', 'input.csv')
    else:
        log_lines.append('Move failed')

    # Write output files
    write_text(txt_out, '\n'.join(log_lines))
    write_csv(csv_out, [['status', 'detail']] + [[str(i), line] for i, line in enumerate(log_lines, 1)])

    # Demonstrate delete (clean up archived file)
    deleted = delete_file(csv_in)
    log_lines.append(f'Delete archived CSV: {deleted}')

    # Append final status to output
    append_text(txt_out, '\nFinal cleanup complete.\n')

    return {
        'txt_out': txt_out,
        'csv_out': csv_out,
        'log': log_lines,
    }


if __name__ == '__main__':
    print('Running demo_operations()...')
    result = demo_operations()
    print('Outputs written:')
    print(result['txt_out'])
    print(result['csv_out'])
