

if __name__ == "__main__":
    grid = []
    with open('6.txt', 'r') as f:
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
        for x in range(len(grid[i])):
            if grid[i][x] == '*':
                found_number_idxs = set()
                for dy, dx in directions:
                    if (i+dy >= 0) and (i+dy < len(grid)) and (x+dx >= 0) and (x+dx < len(grid[i])):
                        if grid[i+dy][x+dx].isdigit():
                            start_x = 0
                            for scan_x in range(x+dx, -1, -1):
                                if not grid[i+dy][scan_x].isdigit():
                                    start_x = scan_x+1
                                    break
                            end_x = len(grid[i+dy])
                            for scan_x in range(x+dx, len(grid[i+dy])):
                                if not grid[i+dy][scan_x].isdigit():
                                    end_x = scan_x-1
                                    break
                            found_number_idxs.add((start_x, end_x, i+dy))
                
                if len(found_number_idxs) == 2:
                    gear_ratio = 1
                    for start_x, end_x, y_idx in found_number_idxs:
                        gear_ratio *= int(grid[y_idx][start_x:end_x+1])
                
                    total += gear_ratio

    print(total)

