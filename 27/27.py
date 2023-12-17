
if __name__ == "__main__":
    grid = []
    with open('27.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())

    h, w = len(grid), len(grid[0])
    curr_row = [0 for _ in range(w)]
    total = 0
    for row_idx in range(h):
        for col_idx in range(w):
            if grid[row_idx][col_idx] == 'O':
                total += h - curr_row[col_idx]
                curr_row[col_idx] += 1
            elif grid[row_idx][col_idx] == '#':
                curr_row[col_idx] = row_idx + 1
    
    print(total)
