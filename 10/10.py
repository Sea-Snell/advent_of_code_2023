
if __name__ == "__main__":
    with open('10.txt', 'r') as f:
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
                map_values.append(tuple(map_item))
            map_hierarchy.append(set(map_values))
        
    curr_seed_ranges = set(zip(seeds[::2], seeds[1::2]))
    for map_values in map_hierarchy:
        new_seed_ranges = set()
        while len(curr_seed_ranges) > 0:
            seed_range_start, seed_range_delta = curr_seed_ranges.pop()
            found_match = False
            for dest_start, source_start, delta in map_values:
                if seed_range_start >= source_start and seed_range_start < (source_start+delta):
                    if (seed_range_start+seed_range_delta) <= (source_start+delta):
                        new_seed_ranges.add(((seed_range_start-source_start)+dest_start, seed_range_delta))
                    else:
                        new_seed_ranges.add(((seed_range_start-source_start)+dest_start, source_start+delta-seed_range_start))
                        curr_seed_ranges.add((source_start+delta, (seed_range_start+seed_range_delta)-(source_start+delta)))
                    found_match = True
                    break
                elif (seed_range_start+seed_range_delta) > source_start and (seed_range_start+seed_range_delta) <= (source_start+delta):
                    new_seed_ranges.add((dest_start, seed_range_start+seed_range_delta-source_start))
                    curr_seed_ranges.add((seed_range_start, source_start-seed_range_start))
                    found_match = True
                    break
            if not found_match:
                new_seed_ranges.add((seed_range_start, seed_range_delta))
        curr_seed_ranges = new_seed_ranges
    
    print(min(list(zip(*curr_seed_ranges))[0]))
