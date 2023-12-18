
if __name__ == "__main__":
    with open('29.txt', 'r') as f:
        instructions = f.read()
    instructions = instructions.replace('\n', '')
    instructions = list(map(lambda x: x.strip(), instructions.split(',')))

    total = 0
    for instruction in instructions:
        hash_val = 0
        for c in instruction:
            hash_val = ((hash_val + ord(c)) * 17) % 256
        total += hash_val
    
    print(total)
