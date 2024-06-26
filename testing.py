import unittest
from app import get_request


class TestFileName(unittest.TestCase):
    def test_get_request(self):
        self.assertEqual(get_request(
          "http://export.arxiv.org/api/query",
          {"search_query": "all:machine learning",
              "start": 0,
              "max_results": 5}),
          "Request successful!")


if __name__ == '__main__':
    unittest.main()
