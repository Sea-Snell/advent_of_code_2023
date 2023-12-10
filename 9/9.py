
if __name__ == "__main__":
    with open('9.txt', 'r') as f:
        seeds = f.readline()
        seeds = list(map(int, filter(lambda x: len(x) > 0, seeds.split(':')[1].strip().split(' '))))
        _ = f.readline() # newline

        map_hierarchy = []
        while True:
            map_title = f.readline() # map title
            if len(map_title.strip()) == 0:
                break
            map_values = []
            for line in f:
                if len(line.strip()) == 0:
                    break
                map_item = list(map(int, filter(lambda x: len(x) > 0, line.strip().split(' '))))
                map_values.append(map_item)
            map_hierarchy.append(map_values)
        
    locations = []
    for seed in seeds:
        curr_value = seed
        for map_values in map_hierarchy:
            for dest_start, source_start, delta in map_values:
                if curr_value >= source_start and curr_value < (source_start+delta):
                    curr_value = (curr_value-source_start)+dest_start
                    break
        locations.append(curr_value)
    print(min(locations))
