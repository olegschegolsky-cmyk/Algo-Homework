from lab1 import snake
import unittest

class Ts(unittest.TestCase):
    def test_3_3_custom(self):
        m, n = 3, 3
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        res = snake(matrix, m, n)
        print(f"Результат 3x3: {res}")

    def test_2_4(self):
        m, n = 2, 4
        matrix = [[1, 2, 3, 4], 
                  [5, 6, 7, 8]]
        res = snake(matrix, m, n)
        print(f"Результат 2x4: {res}")

unittest.main()