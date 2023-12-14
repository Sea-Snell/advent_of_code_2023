
from collections import deque

if __name__ == "__main__":
    with open('20.txt', 'r') as f:
        pipes = []
        for line in f:
            pipes.append(line.strip())

    start_pos = None
    for i, pipe_row in enumerate(pipes):
        if 'S' in pipe_row:
            start_pos = (i, pipe_row.index('S'))
            break
    assert start_pos is not None

    deltas = {
        '|': [(1, 0), (-1, 0)],
        '-': [(0, 1), (0, -1)],
        'L': [(0, 1), (-1, 0)],
        'J': [(0, -1), (-1, 0)],
        '7': [(0, -1), (1, 0)],
        'F': [(0, 1), (1, 0)],
    }

    valid_next_pipes = {
        (1, 0): '|LJ',
        (-1, 0): '|7F',
        (0, 1): '-7J',
        (0, -1): '-FL',
    }

    max_loop_size, true_pipes = 0, None
    for start_pipe in deltas.keys():
        curr_pipes = list(pipes)
        curr_pipes[start_pos[0]] = curr_pipes[start_pos[0]].replace('S', start_pipe)
        last_pos, curr_pos = None, start_pos
        visited = set()

        invalid = False
        for delta in deltas[start_pipe]:
            new_pos = (curr_pos[0]+delta[0], curr_pos[1]+delta[1])
            if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(curr_pipes) or new_pos[1] >= len(curr_pipes[new_pos[0]]):
                continue
            next_pipe = curr_pipes[new_pos[0]][new_pos[1]]
            if not (next_pipe in valid_next_pipes[delta]):
                invalid = True
        
        if invalid:
            continue

        while not (curr_pos in visited):
            if curr_pipes[curr_pos[0]][curr_pos[1]] in deltas.keys():
                found_new_pos = False
                for direction in deltas[curr_pipes[curr_pos[0]][curr_pos[1]]]:
                    new_pos = (curr_pos[0]+direction[0], curr_pos[1]+direction[1])
                    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(curr_pipes) or new_pos[1] >= len(curr_pipes[new_pos[0]]):
                        continue
                    if new_pos != last_pos:
                        visited.add(curr_pos)
                        curr_pos, last_pos = new_pos, curr_pos
                        found_new_pos = True
                        break
                if not found_new_pos:
                    break
            else:
                break
        
        if curr_pos == start_pos:
            loop_size = len(visited)
            if loop_size > max_loop_size:
                max_loop_size = loop_size
                true_pipes = list(curr_pipes)
                for i in range(len(true_pipes)):
                    true_pipes[i] = list(true_pipes[i])
                    for j in range(len(true_pipes[i])):
                        if not ((i, j) in visited):
                            true_pipes[i][j] = '.'
                    true_pipes[i] = ''.join(true_pipes[i])
    
    expanded_map = []
    for i in range(len(true_pipes)):
        new_row = []
        for j in range(len(true_pipes[i])):
            new_row.append(true_pipes[i][j])
            if true_pipes[i][j] in '-FL':
                new_row.append('-')
            else:
                new_row.append('.')
        expanded_map.append(''.join(new_row))
        new_new_row = []
        for j in range(len(new_row)):
            if new_row[j] in '|F7':
                new_new_row.append('|')
            else:
                new_new_row.append('.')
        expanded_map.append(''.join(new_new_row))
    
    connected_components = []
    visited = set()
    for i in range(len(expanded_map)):
        for j in range(len(expanded_map[i])):
            if expanded_map[i][j] == '.' and (not ((i, j) in visited)):
                component = set()
                q = deque([(i, j)])
                while len(q) > 0:
                    curr_node = q.popleft()
                    if curr_node in component:
                        continue
                    component.add(curr_node)
                    for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_node = (curr_node[0]+delta[0], curr_node[1]+delta[1])
                        if new_node[0] < 0 or new_node[1] < 0 or new_node[0] >= len(expanded_map) or new_node[1] >= len(expanded_map[new_node[0]]):
                            continue
                        if expanded_map[new_node[0]][new_node[1]] == '.':
                            q.append(new_node)
                visited |= component
                connected_components.append(component)

    all_points_contained = []
    for component in connected_components:
        hits_edge = False
        for item in component:
            if item[0] == 0 or item[1] == 0 or item[0] == (len(expanded_map)-1) or item[1] == (len(expanded_map[item[0]])-1):
                hits_edge = True
        if not hits_edge:
            points_contained = 0
            for item in component:
                if (item[0] % 2 == 0) and (item[1] % 2 == 0):
                    points_contained += 1
            all_points_contained.append(points_contained)
    
    assert len(all_points_contained) == 1
    print(all_points_contained[0])
