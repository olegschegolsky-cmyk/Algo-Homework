import csv

def read_matrix_from_csv(file_path):
    matrix = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append([int(cell) for cell in row])
    return matrix


def calculate_minimum_cable_length(matrix):
    n = len(matrix)
    if n <= 1:
        return 0

    visited = [False] * n
    visited[0] = True
    total_length = 0
    edges_used = 0

    while edges_used < n - 1:
        min_edge = float("inf")
        next_node = -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and matrix[i][j] > 0:
                        if matrix[i][j] < min_edge:
                            min_edge = matrix[i][j]
                            next_node = j

        if next_node != -1:
            visited[next_node] = True
            total_length += min_edge
            edges_used += 1
        else:
            break

    return total_length