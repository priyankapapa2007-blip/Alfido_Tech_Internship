import os
import tempfile
import unittest

from file_utils import (
    read_text,
    write_text,
    append_text,
    read_csv,
    write_csv,
    move_file,
    rename_file,
    delete_file,
)


class FileUtilsTest(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.tmpdir = tempfile.TemporaryDirectory()
        self.base = self.tmpdir.name

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_text_read_write_append(self):
        p = os.path.join(self.base, 'a', 't.txt')
        self.assertTrue(write_text(p, 'line1\n'))
        self.assertEqual(read_text(p), 'line1\n')
        self.assertTrue(append_text(p, 'line2\n'))
        self.assertIn('line2', read_text(p))

    def test_csv_read_write(self):
        p = os.path.join(self.base, 'd', 'x.csv')
        rows = [['h1', 'h2'], ['v1', 'v2']]
        self.assertTrue(write_csv(p, rows))
        got = read_csv(p)
        self.assertEqual(got, rows)

    def test_move_rename_delete(self):
        src = os.path.join(self.base, 'src.txt')
        write_text(src, 'hi')
        # rename
        new_path = rename_file(src, 'renamed.txt')
        self.assertTrue(os.path.exists(new_path))
        # move
        dst = os.path.join(self.base, 'sub', 'moved.txt')
        self.assertTrue(move_file(new_path, dst))
        self.assertTrue(os.path.exists(dst))
        # delete
        self.assertTrue(delete_file(dst))
        self.assertFalse(os.path.exists(dst))


if __name__ == '__main__':
    unittest.main()
