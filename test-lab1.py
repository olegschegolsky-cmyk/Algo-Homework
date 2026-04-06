from lab1 import hamsters
import unittest

class TestHamsters(unittest.TestCase):
    
    def test_example_1(self):
        S = 7
        C = 3
        hamster = [[1, 2], 
                   [2, 2], 
                   [3, 1]]

    def test_example_2(self):
        S = 19
        C = 4
        hamster = [[5, 0], 
                   [2, 2], 
                   [1, 4], 
                   [5, 1]]

    def test_example_3(self):
        S = 2
        C = 2
        hamster = [[1, 50], 
                   [1, 60]]
    def test_example_4(self):
        S = 32
        C = 2
        hamster = [[1, 2], 
                   [3, 4],
                   [5, 6]]

    def test_zero_food(self):
        S = 0
        C = 3
        hamster = [[1, 1], 
                   [2, 2], 
                   [3, 3]]

unittest.main()