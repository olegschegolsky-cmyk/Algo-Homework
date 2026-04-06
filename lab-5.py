import ast
import unittest

def flood_fill(matrix, r, c, target_color, replacement_color):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
        return
    if matrix[r][c] != target_color:
        return
    if target_color == replacement_color:
        return

    matrix[r][c] = replacement_color

    flood_fill(matrix, r - 1, c, target_color, replacement_color)
    flood_fill(matrix, r + 1, c, target_color, replacement_color)
    flood_fill(matrix, r, c - 1, target_color, replacement_color)
    flood_fill(matrix, r, c + 1, target_color, replacement_color)

try:
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    h, w = map(int, lines[0].split(','))
    start_r, start_c = map(int, lines[1].split(','))
    replacement_color = lines[2].replace("'", "").replace('"', '').replace('‘', '').replace('’', '')

    matrix = []
    for line in lines[3:]:
        if line.endswith(','):
            line = line[:-1]
        line = line.replace('‘', "'").replace('’', "'")
        row = ast.literal_eval(line)
        matrix.append(row)

    target_color = matrix[start_r][start_c]
        
    flood_fill(matrix, start_r, start_c, target_color, replacement_color)

    with open('output.txt', 'w', encoding='utf-8') as f:
        for row in matrix:
            formatted_row = "['" + "', '".join(row) + "']"
            f.write(formatted_row + '\n')

except Exception:
    pass

class TestFloodFill(unittest.TestCase):
    def test_basic_fill(self):
        matrix = [
            ['A', 'A', 'B'],
            ['A', 'B', 'B'],
            ['B', 'B', 'A']
        ]
        flood_fill(matrix, 0, 0, 'A', 'C')
        expected = [
            ['C', 'C', 'B'],
            ['C', 'B', 'B'],
            ['B', 'B', 'A']
        ]
        self.assertEqual(matrix, expected)

    def test_no_change_needed(self):
        matrix = [['A', 'A'], ['A', 'A']]
        flood_fill(matrix, 0, 0, 'A', 'A')
        expected = [['A', 'A'], ['A', 'A']]
        self.assertEqual(matrix, expected)

    def test_out_of_bounds_handling(self):
        matrix = [['A']]
        flood_fill(matrix, 5, 5, 'A', 'C')
        expected = [['A']]
        self.assertEqual(matrix, expected)

unittest.main()