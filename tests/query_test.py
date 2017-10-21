import unittest
from douban_rating.query import query


class TestQuery(unittest.TestCase):
    def test_query(self):
        query_type = 'book'
        title = 'flask'
        ratings = query(query_type, title)

        self.assertTrue(len(ratings) > 0)

if __name__ == '__main__':
    unittest.main()
