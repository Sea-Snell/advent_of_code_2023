
if __name__ == "__main__":
    cosmic_map = []
    with open('22.txt', 'r') as f:
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
    
    expansion_factor = 1000000

    galacy_idxs = []
    for i in range(len(cosmic_map)):
        for j in range(len(cosmic_map[i])):
            if cosmic_map[i][j] == '#':
                galacy_idxs.append((i, j))
    
    total = 0
    for i in range(len(galacy_idxs)):
        for j in range(i+1, len(galacy_idxs)):
            total += abs(galacy_idxs[i][0] - galacy_idxs[j][0]) + abs(galacy_idxs[i][1] - galacy_idxs[j][1])
            for empty_row in empty_rows:
                if empty_row > min(galacy_idxs[i][0], galacy_idxs[j][0]) and empty_row < max(galacy_idxs[i][0], galacy_idxs[j][0]):
                    total += (expansion_factor-1)
            for empty_column in empty_columns:
                if empty_column > min(galacy_idxs[i][1], galacy_idxs[j][1]) and empty_column < max(galacy_idxs[i][1], galacy_idxs[j][1]):
                    total += (expansion_factor-1)

    print(total)
