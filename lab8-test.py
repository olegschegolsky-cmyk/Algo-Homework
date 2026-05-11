import unittest
from lab8 import count_paths

class TestIndianaJones(unittest.TestCase):
    
    def test_first_example(self):
        W = 3
        H = 3
        grid = ["aaa", "cab", "def"]
        result = count_paths(W, H, grid)
        self.assertEqual(result, 5)

    def test_second_example(self):
        W = 10
        H = 1
        grid = ["abcdefaghi"]
        result = count_paths(W, H, grid)
        self.assertEqual(result, 2)

    def test_third_example(self):
        W = 7
        H = 6
        grid = [
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa"
        ]
        result = count_paths(W, H, grid)
        self.assertEqual(result, 201684)

if __name__ == '__main__':
    unittest.main()