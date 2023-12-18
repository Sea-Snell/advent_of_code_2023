
def hash_alg(label):
    hash_val = 0
    for c in label:
        hash_val = ((hash_val + ord(c)) * 17) % 256
    return hash_val

if __name__ == "__main__":
    with open('30.txt', 'r') as f:
        instructions = f.read()
    instructions = instructions.replace('\n', '')
    instructions = list(map(lambda x: x.strip(), instructions.split(',')))

    bins = [[] for _ in range(256)]
    for instruction in instructions:        
        if '-' in instruction:
            label = instruction.split('-')[0]
            hash_val = hash_alg(label)
            curr_bin = bins[hash_val]
            for item_label, item_lense in curr_bin:
                if item_label == label:
                    curr_bin.remove((item_label, item_lense))
                    break
        elif '=' in instruction:
            label, lense = instruction.split('=')
            lense = int(lense)
            hash_val = hash_alg(label)
            curr_bin = bins[hash_val]
            found = False
            for idx, (item_label, item_lense) in enumerate(curr_bin):
                if item_label == label:
                    curr_bin[idx] = (label, lense)
                    found = True
                    break
            if not found:
                curr_bin.append((label, lense))
        else:
            raise NotImplementedError
    
    total = 0
    for bin_idx in range(len(bins)):
        for lense_idx in range(len(bins[bin_idx])):
            total += (bin_idx+1)*(lense_idx+1)*bins[bin_idx][lense_idx][1]

    print(total)
