def cumsum(a):
    total = 0
    items = []
    for item in a:
        total += item
        items.append(total)
    return items

if __name__ == "__main__":
    moves = []
    with open('35.txt', 'r') as f:
        for line in f:
            direction, num, _ = line.strip().split()
            moves.append((direction, int(num)))
    
    x_corrds = cumsum([num * int(dir == 'R') - num * int(dir == 'L') for dir, num in moves])
    y_corrrds = cumsum([num * int(dir == 'U') - num * int(dir == 'D') for dir, num in moves])

    min_x, max_x = min(x_corrds), max(x_corrds)
    min_y, max_y = min(y_corrrds), max(y_corrrds)

    is_filled = [[False for _ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]
    is_filled[0-min_y][0-min_x] = True

    curr_x, curr_y = 0, 0
    for dir, num in moves:
        for i in range(1, num+1):
            new_x = curr_x + i * int(dir == 'R') - i * int(dir == 'L')
            new_y = curr_y + i * int(dir == 'U') - i * int(dir == 'D')
            is_filled[new_y-min_y][new_x-min_x] = True
        curr_x, curr_y = new_x, new_y

    def next_nodes(node):
        directions = [
            (1, 0),
            (-1, 0), 
            (0, 1),
            (0, -1),
        ]
        new_nodes = []
        for dy, dx in directions:
            new_node = (node[0]+dy, node[1]+dx)
            if new_node[0] >= 0 and new_node[1] >= 0 and new_node[0] < len(is_filled) and new_node[1] < len(is_filled[new_node[0]]) and (not is_filled[new_node[0]][new_node[1]]):
                new_nodes.append((node[0]+dy, node[1]+dx))
        return new_nodes
    
    visited = set()
    main_cluster = None
    for i in range(len(is_filled)):
        for j in range(len(is_filled[i])):
            if not is_filled[i][j]:
                if (i, j) in visited:
                    continue
                curr_cluster = set()
                stack = [(i, j)]
                while len(stack) > 0:
                    curr_node = stack.pop()
                    if curr_node in visited:
                        continue
                    visited.add(curr_node)
                    curr_cluster.add(curr_node)
                    for next_node in next_nodes(curr_node):
                        stack.append(next_node)
                
                has_edge = False
                for y, x in curr_cluster:
                    if y == 0 or x == 0 or y == len(is_filled)-1 or x == len(is_filled[y])-1:
                        has_edge = True
                if not has_edge:
                    main_cluster = curr_cluster
                    break
    
    for y, x in main_cluster:
        is_filled[y][x] = True
    
    print(sum(sum(is_filled, [])))
