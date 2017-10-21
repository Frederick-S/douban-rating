import io
import sys
import unittest
from contextlib import redirect_stdout
from douban_rating.main import main


class TestCli(unittest.TestCase):
    def test_invalid_query_type(self):
        sys.argv[1:] = []
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertEqual(
            'Usage: douban-rating -book book-name\n', f.getvalue())

        sys.argv[1:] = ['-music', 'flask']
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertEqual('Invalid type\n', f.getvalue())

        sys.argv[1:] = ['-book', 'flask']
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertTrue(f.getvalue().index('Flask') > 0)

if __name__ == '__main__':
    unittest.main()
