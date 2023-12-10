
if __name__ == "__main__":
    with open('15.txt', 'r') as f:
        instructions = [0 if inst == 'L' else 1 for inst in f.readline().strip()]
        _ = f.readline()
        graph = {}
        for line in f:
            node, connections = line.split(' = ')
            node = node.strip()
            l_connection, r_connection = connections.strip().split(', ')
            l_connection = l_connection[1:]
            r_connection = r_connection[:-1]
            graph[node] = (l_connection, r_connection)
        
    connection_from_each_start_node = {}
    for start_node in graph.keys():
        curr_node = start_node
        for instruction in instructions:
            curr_node = graph[curr_node][instruction]
        connection_from_each_start_node[start_node] = curr_node

    curr_node = 'AAA'
    step_count = 0
    while curr_node != 'ZZZ':
        curr_node = connection_from_each_start_node[curr_node]
        step_count += len(instructions)
    print(step_count)