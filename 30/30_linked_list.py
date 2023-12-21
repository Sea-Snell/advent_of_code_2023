# bored on a plane with no wifi, so I wrote a more efficient linked list version of 30

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

    bins, bin_link_by_id = [None for _ in range(256)], dict()
    for instruction in instructions:        
        if '-' in instruction:
            label = instruction.split('-')[0]
            hash_idx = hash_alg(label)
            if label in bin_link_by_id:
                link = bin_link_by_id.pop(label)
                if link[2] is None:
                    bins[hash_idx] = link[1]
                if not (link[1] is None):
                    link[1][2] = link[2]
                if not (link[2] is None):
                    link[2][1] = link[1]
        elif '=' in instruction:
            label, lense = instruction.split('=')
            hash_idx = hash_alg(label)
            if label in bin_link_by_id:
                bin_link_by_id[label][0] = (label, lense)
            else:
                new_link = [(label, lense), bins[hash_idx], None]
                if not (bins[hash_idx] is None):
                    bins[hash_idx][2] = new_link
                bins[hash_idx] = new_link
                bin_link_by_id[label] = new_link
        else:
            raise NotImplementedError

    total = 0
    for bin_idx, curr_node in enumerate(bins):
        bin_total = 0
        while curr_node is not None:
            bin_total += int(curr_node[0][1])
            total += (bin_idx+1)*bin_total
            curr_node = curr_node[1]
    print(total)
