

if __name__ == "__main__":
    patterns = []
    with open('26.txt', 'r') as f:
        curr_pattern = []
        for line in f:
            if line.strip() == '':
                patterns.append(curr_pattern)
                curr_pattern = []
            else:
                curr_pattern.append(line.strip())
        if len(curr_pattern) > 0:
            patterns.append(curr_pattern)


    total = 0
    for pattern in patterns:
        pattern_height, pattern_width = len(pattern), len(pattern[0])

        vertical_memo = [[-1 for size in range(min(center, pattern_width-center)+1)] for center in range(1, pattern_width)]
        for center in range(1, pattern_width):
            vertical_memo[center-1][0] = 0

        for center in range(1, pattern_width):
            for size in range(1, min(center, pattern_width-center)+1):
                if vertical_memo[center-1][size-1] >= 0:
                    left_col = [row[center-size] for row in pattern]
                    right_col = [row[center+(size-1)] for row in pattern]
                    col_dis = sum([a != b for a, b in zip(left_col, right_col)])
                    if col_dis == 0:
                        vertical_memo[center-1][size] = vertical_memo[center-1][size-1]
                    elif col_dis == 1:
                        if vertical_memo[center-1][size-1] == 1:
                            vertical_memo[center-1][size] = -1
                        else:
                            vertical_memo[center-1][size] = 1
        
        horizontal_memo = [[-1 for size in range(min(center, pattern_height-center)+1)] for center in range(1, pattern_height)]
        for center in range(1, pattern_height):
            horizontal_memo[center-1][0] = 0
        
        for center in range(1, pattern_height):
            for size in range(1, min(center, pattern_height-center)+1):
                if horizontal_memo[center-1][size-1] >= 0:
                    top_row = pattern[center-size]
                    bottom_row = pattern[center+(size-1)]
                    row_dist = sum([a != b for a, b in zip(top_row, bottom_row)])
                    if row_dist == 0:
                        horizontal_memo[center-1][size] = horizontal_memo[center-1][size-1]
                    elif row_dist == 1:
                        if horizontal_memo[center-1][size-1] == 1:
                            horizontal_memo[center-1][size] = -1
                        else:
                            horizontal_memo[center-1][size] = 1
        
        vertical_mirror, horizontal_mirror = None, None
        for center in range(1, pattern_width):
            if vertical_memo[center-1][-1] == 1:
                vertical_mirror = center
                break
        for center in range(1, pattern_height):
            if horizontal_memo[center-1][-1] == 1:
                horizontal_mirror = center
                break
        
        assert not ((vertical_mirror is None) and (horizontal_mirror is None))
        assert not ((vertical_mirror is not None) and (horizontal_mirror is not None))

        if vertical_mirror is None:
            total += horizontal_mirror * 100
        elif horizontal_mirror is None:
            total += vertical_mirror
    
    print(total)
