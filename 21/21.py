
if __name__ == "__main__":
    cosmic_map = []
    with open('21.txt', 'r') as f:
        for line in f:
            cosmic_map.append(line.strip())
    
    empty_rows = set()
    empty_columns = set()

    for i, row in enumerate(cosmic_map):
        if all(map(lambda x: x == '.', row)):
            empty_rows.add(i)
    
    for i in range(len(cosmic_map[0])):
        if all(map(lambda x: x == '.', map(lambda y: y[i], cosmic_map))):
            empty_columns.add(i)
    
    expanded_map = []
    for i in range(len(cosmic_map)):
        expanded_map.append([])
        for j in range(len(cosmic_map[i])):
            expanded_map[-1].append(cosmic_map[i][j])
            if j in empty_columns:
                expanded_map[-1].append(cosmic_map[i][j])
        if i in empty_rows:
            new_row = list(expanded_map[-1])
            expanded_map.append(new_row)
    
    expanded_map = list(map(lambda x: ''.join(x), expanded_map))

    galacy_idxs = []
    for i in range(len(expanded_map)):
        for j in range(len(expanded_map[i])):
            if expanded_map[i][j] == '#':
                galacy_idxs.append((i, j))
    
    total = 0
    for i in range(len(galacy_idxs)):
        for j in range(i+1, len(galacy_idxs)):
            total += abs(galacy_idxs[i][0] - galacy_idxs[j][0]) + abs(galacy_idxs[i][1] - galacy_idxs[j][1])

    print(total)
