
if __name__ == "__main__":
    total = 0
    with open('7.txt', 'r') as f:
        for line in f:
            hand, winning = line.split(':')[1].split('|')
            hand = list(filter(lambda x: len(x) > 0, hand.strip().split(' ')))
            winning = list(filter(lambda x: len(x) > 0, winning.strip().split(' ')))
            winning = set(winning)
            matched = 0
            for num in hand:
                if num in winning:
                    matched += 1
            if matched > 0:
                total += 2**(matched-1)
    print(total)
