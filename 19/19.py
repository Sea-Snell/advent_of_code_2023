
if __name__ == "__main__":
    with open('19.txt', 'r') as f:
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

    max_loop_size = 0
    for start_pipe in deltas.keys():
        curr_pipes = list(pipes)
        curr_pipes[start_pos[0]] = curr_pipes[start_pos[0]].replace('S', start_pipe)
        last_pos, curr_pos = None, start_pos
        visited = set()

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
            max_loop_size = max(max_loop_size, loop_size)
    
    print(max_loop_size // 2)