def snake(matrix, m, n):
    result = []
    row = 0
    col = 0
    
    t_elem = m * n
    
    for i in range(t_elem):
        result.append(matrix[row][col])
 
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
                
    return result

