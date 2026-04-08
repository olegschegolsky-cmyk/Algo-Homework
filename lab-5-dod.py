import os
import time
from collections import deque

def print_maze(maze, delay=0):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in maze:
        print(" ".join(row))
    print("\n")
    time.sleep(delay)

def solve_maze_bfs(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    start = None
    end = None
    
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'A':
                start = (r, c)
            elif maze[r][c] == 'B':
                end = (r, c)
                
    if not start or not end:
        return

    queue = deque([start])
    came_from = {start: None}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            break
            
        r, c = current
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] in ['.', 'B'] and (nr, nc) not in came_from:
                    queue.append((nr, nc))
                    came_from[(nr, nc)] = current
                    
                    if maze[nr][nc] != 'B':
                        maze[nr][nc] = '~'
                        print_maze(maze)

    if end in came_from:
        curr = came_from[end]
        while curr != start:
            r, c = curr
            maze[r][c] = '*'
            print_maze(maze)
            curr = came_from[curr]

maze = [
    ['A', '.', '.', 'W', '.', '.', '.', 'W', '.'],
    ['W', 'W', '.', 'W', '.', 'W', '.', 'W', '.'],
    ['.', '.', '.', '.', '.', 'W', '.', '.', '.'],
    ['.', 'W', 'W', 'W', '.', 'W', 'W', 'W', '.'],
    ['.', '.', '.', 'W', '.', '.', '.', '.', 'B']
]

print_maze(maze, 1.0)
solve_maze_bfs(maze)