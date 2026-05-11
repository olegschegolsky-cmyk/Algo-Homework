def count_paths(W, H, grid):
    S = [0] * 256
    prev_col = [1] * H

    for r in range(H):
        S[ord(grid[r][0])] += 1

    for c in range(1, W):
        curr_col = [0] * H
        new_S = [0] * 256

        for r in range(H):
            char_idx = ord(grid[r][c])
            val = S[char_idx]

            if grid[r][c] != grid[r][c-1]:
                val += prev_col[r]

            curr_col[r] = val
            new_S[char_idx] += val

        for i in range(256):
            S[i] += new_S[i]

        prev_col = curr_col

    if H == 1:
        return prev_col[0]
    else:
        return prev_col[0] + prev_col[H-1]

if __name__ == '__main__':
    with open('ijones.in', 'r') as f:
        data = f.read().split()
        
    W = int(data[0])
    H = int(data[1])
    grid = data[2:]
    
    ans = count_paths(W, H, grid)
    
    with open('ijones.out', 'w') as f:
        f.write(str(ans))