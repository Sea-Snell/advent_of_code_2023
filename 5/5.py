

if __name__ == "__main__":
    grid = []
    with open('5.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())
    
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]
    
    total = 0
    for i in range(len(grid)):
        num_start_idx, has_symbol = None, False
        for x in range(len(grid[i])):
            if grid[i][x].isdigit():
                if num_start_idx is None:
                    num_start_idx = x
                for dy, dx in directions:
                    if (i + dy >= 0) and (i + dy < len(grid)) and (x + dx >= 0) and (x + dx < len(grid[i])):
                        grid_char = grid[i + dy][x + dx]
                        if (not grid_char.isdigit()) and (grid_char != '.'):
                            has_symbol = True
                            break
            else:
                if num_start_idx is not None:
                    if has_symbol:
                        num_value = int(grid[i][num_start_idx:x])
                        total += num_value
                    num_start_idx, has_symbol = None, False
        if num_start_idx is not None:
            if has_symbol:
                num_value = int(grid[i][num_start_idx:(x+1)])
                total += num_value
            num_start_idx, has_symbol = None, False
    
    print(total)

