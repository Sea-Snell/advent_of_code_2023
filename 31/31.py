# I code golfed this one a bit for fun because I'm stuck on a flight with bad wifi and there's nothing else to do

if __name__ == "__main__":
    with open('31.txt', 'r') as f:
        grid = [line.strip() for line in f]
    
    visited, node_stack = set(), [(0, 0, 0, 1)]

    transform_check = lambda i: i[0] >= 0 and i[1] >= 0 and i[0] < len(grid) and i[1] < len(grid[i[0]]) and (i[2]+i[3]) != 0 and (i[2]*i[3]) == 0

    transforms = {
        '.': lambda y, x, dy, dx: list(filter(transform_check, [(y+dy, x+dx, dy, dx)])),
        '/': lambda y, x, dy, dx: list(filter(transform_check, [(y-dx, x-dy, -dx, -dy)])),
        '\\': lambda y, x, dy, dx: list(filter(transform_check, [(y+dx, x+dy, dx, dy)])),
        '-': lambda y, x, dy, dx: list(filter(transform_check, [(y, x+min(dx+1, 1), 0, min(dx+1, 1)), (y, x+max(dx-1, -1), 0, max(dx-1, -1))])),
        '|': lambda y, x, dy, dx: list(filter(transform_check, [(y+min(dy+1, 1), x, min(dy+1, 1), 0), (y+max(dy-1, -1), x, max(dy-1, -1), 0)])),
    }

    while len(node_stack) > 0:
        y, x, dy, dx = node_stack.pop()
        if (y, x, dy, dx) in visited:
            continue
        visited.add((y, x, dy, dx))
        node_stack.extend(transforms[grid[y][x]](y, x, dy, dx))
    
    print(len(set([(y, x) for y, x, _, _ in visited])))
