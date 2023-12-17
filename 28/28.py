
def tilt_up(grid):
    h, w = len(grid), len(grid[0])
    curr_row = [0 for _ in range(w)]
    new_grid = [list(row) for row in grid]
    for row_idx in range(h):
        for col_idx in range(w):
            if grid[row_idx][col_idx] == 'O':
                new_grid[row_idx][col_idx] = '.'
                new_grid[curr_row[col_idx]][col_idx] = 'O'
                curr_row[col_idx] += 1
            elif grid[row_idx][col_idx] == '#':
                curr_row[col_idx] = row_idx + 1
    return [''.join(row) for row in new_grid]

def tilt_down(grid):
    h, w = len(grid), len(grid[0])
    curr_row = [h-1 for _ in range(w)]
    new_grid = [list(row) for row in grid]
    for row_idx in range(h-1, -1, -1):
        for col_idx in range(w):
            if grid[row_idx][col_idx] == 'O':
                new_grid[row_idx][col_idx] = '.'
                new_grid[curr_row[col_idx]][col_idx] = 'O'
                curr_row[col_idx] -= 1
            elif grid[row_idx][col_idx] == '#':
                curr_row[col_idx] = row_idx - 1
    return [''.join(row) for row in new_grid]

def tilt_left(grid):
    h, w = len(grid), len(grid[0])
    curr_col = [0 for _ in range(h)]
    new_grid = [list(row) for row in grid]
    for col_idx in range(w):
        for row_idx in range(h):
            if grid[row_idx][col_idx] == 'O':
                new_grid[row_idx][col_idx] = '.'
                new_grid[row_idx][curr_col[row_idx]] = 'O'
                curr_col[row_idx] += 1
            elif grid[row_idx][col_idx] == '#':
                curr_col[row_idx] = col_idx + 1
    return [''.join(row) for row in new_grid]

def tilt_right(grid):
    h, w = len(grid), len(grid[0])
    curr_col = [w-1 for _ in range(h)]
    new_grid = [list(row) for row in grid]
    for col_idx in range(w-1, -1, -1):
        for row_idx in range(h):
            if grid[row_idx][col_idx] == 'O':
                new_grid[row_idx][col_idx] = '.'
                new_grid[row_idx][curr_col[row_idx]] = 'O'
                curr_col[row_idx] -= 1
            elif grid[row_idx][col_idx] == '#':
                curr_col[row_idx] = col_idx - 1
    return [''.join(row) for row in new_grid]

def cycle(grid):
    grid = tilt_up(grid)
    grid = tilt_left(grid)
    grid = tilt_down(grid)
    grid = tilt_right(grid)
    return grid

if __name__ == "__main__":
    grid = []
    with open('28.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    
    visited_grids = dict()
    grid_hash = '\n'.join(grid)
    while not (grid_hash in visited_grids):
        visited_grids[grid_hash] = len(visited_grids)
        grid = cycle(grid)
        grid_hash = '\n'.join(grid)
    
    loop_start = visited_grids[grid_hash]
    loop_size = len(visited_grids) - loop_start
    to_mod = 1000000000 - loop_start
    endpoint = (to_mod % loop_size) + loop_start

    for grid_hash, idx in visited_grids.items():
        if idx == endpoint:
            break

    grid = grid_hash.split('\n')
    h, w = len(grid), len(grid[0])

    total = 0
    for row_idx in range(h):
        for col_idx in range(w):
            if grid[row_idx][col_idx] == 'O':
                total += h - row_idx
    
    print(total)