import unittest

def dr_snake(matrix, m, n, batter):
    proces = []
    cnt = 0
    
    row = 0
    col = 0
    
    t_elem = m * n
    
    for i in range(t_elem):
        ener = matrix[row][col]
        if batter >= ener:
            batter -= ener
            cnt += 1
            proces.append(ener)
        else:
            break 

        if (row + col) % 2 == 0:
            if col == n - 1:
                row += 1
            elif row == 0:
                col += 1
            else:
                row -= 1
                col += 1
        else:
            if row == m - 1:
                col += 1
            elif col == 0:
                row += 1
            else:
                row += 1
                col -= 1
                
    return cnt, batter, proces

class Ts(unittest.TestCase):
    
    def test_dr_f(self):
        m, n = 3, 3
        matrix = [[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]]
        
        bat_1 = 50
        cnt, left, path = dr_snake(matrix, m, n, bat_1)
        print(f"обр {cnt}")
        print(f"залиш {left}")

    def test_dr_sm(self):
        m, n = 3, 3
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        bat_1 = 10
        cnt, left, path = dr_snake(matrix, m, n, bat_1)
        print(f"обр {cnt}")
        print(f"подолано {path}")


try:
    m_in = int(input("рядки m: "))
    n_in = int(input("стовпці n: "))

    matrix_in = []
    print("матриця, числа через пробіл, Enter після кожного рядка ")
    for i in range(m_in):
        row = list(map(int, input().split()))
        matrix_in.append(row)

    print("заряд батареї ")
    batter_in = int(input())

    cnt, left, path = dr_snake(matrix_in, m_in, n_in, batter_in)

    print(f"обр {cnt}")
    print(f"залиш {left}")
    print(f"подолано {path}")

except ValueError:
    print("-")
