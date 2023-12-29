import heapq

if __name__ == "__main__":
    graph = []
    with open('34.txt', 'r') as f:
        for line in f:
            graph.append(line.strip())
    
    directions = [
        (1, 0),
        (-1, 0), 
        (0, 1),
        (0, -1),
    ]

    def next_nodes(curr_node):
        (y, x), (last_dy, last_dx), num_consecutive = curr_node
        next_nodes = []
        for dy, dx in directions:
            new_y, new_x, new_consecutive = y+dy, x+dx, 1
            if dy == last_dy and dx == last_dx:
                new_consecutive = num_consecutive+1
            elif num_consecutive < 4:
                continue
            if new_y >= 0 and new_x >= 0 and new_y < len(graph) and new_x < len(graph[new_y]) and new_consecutive <= 10 and (not (dy == -last_dy and dx == -last_dx)):
                next_nodes.append(((new_y, new_x), (dy, dx), new_consecutive))
        return next_nodes
    
    states_to_check = {item: False for item in sum([[((len(graph)-1, len(graph[len(graph)-1])-1), direction, i) for direction in directions] for i in range(4, 11)], [])}
    h = [(0, 0, ((0, 0), (0, 0), 4), None)]
    visited = dict()
    while len(h) > 0:
        curr_cost, curr_dist, curr_node, prev_node = heapq.heappop(h)
        if curr_node in visited:
            continue
        visited[curr_node] = prev_node
        if curr_node in states_to_check:
            states_to_check[curr_node] = True
        if all(states_to_check.values()):
            break
        for next_node in next_nodes(curr_node):
            new_dist = curr_dist+int(graph[next_node[0][0]][next_node[0][1]])
            new_cost = new_dist+(len(graph)-1-next_node[0][0])+(len(graph[len(graph)-1])-1-next_node[0][1])
            heapq.heappush(h, (new_cost, new_dist, next_node, curr_node))

    min_cost_path = float('inf')
    for state in states_to_check.keys():
        if state in visited:
            path = [state]
            while not (path[-1] is None):
                path.append(visited[path[-1]])
            path.reverse()
            total = 0
            for node, _, _ in path[2:]:
                total += int(graph[node[0]][node[1]])
            min_cost_path = min(min_cost_path, total)
    
    print(min_cost_path)
