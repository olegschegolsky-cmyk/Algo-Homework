import unittest
import os
import csv
from lab7 import read_matrix_from_csv, calculate_minimum_cable_length

class TestVeniceCables(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_islands.csv"
        self.test_matrix = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0],
        ]
        with open(self.test_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(self.test_matrix)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_read_matrix_from_csv(self):
        matrix = read_matrix_from_csv(self.test_filename)
        self.assertEqual(matrix, self.test_matrix)

    def test_calculate_minimum_cable_length(self):
        result = calculate_minimum_cable_length(self.test_matrix)
        self.assertEqual(result, 16)

    def test_single_island(self):
        matrix = [[0]]
        result = calculate_minimum_cable_length(matrix)
        self.assertEqual(result, 0)

    def test_two_islands(self):
        matrix = [[0, 10], [10, 0]]
        result = calculate_minimum_cable_length(matrix)
        self.assertEqual(result, 10)

unittest.main()