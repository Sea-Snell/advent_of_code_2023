
if __name__ == "__main__":
    with open('18.txt', 'r') as f:
        measures = []
        for line in f:
            measures.append(list(map(int, filter(lambda x: len(x) > 0, line.strip().split(' ')))))
    
    total = 0
    for measure in measures:
        diffs = [measure]
        while not all(map(lambda x: x == 0, diffs[-1])):
            new_diff = []
            for a, b in zip(diffs[-1], diffs[-1][1:]):
                new_diff.append(b - a)
            diffs.append(new_diff)
        
        curr = 0
        for diff in diffs[::-1]:
            curr = diff[0] - curr
        total += curr

    print(total)
