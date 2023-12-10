
if __name__ == "__main__":
    matches = []
    with open('8.txt', 'r') as f:
        for line in f:
            hand, winning = line.split(':')[1].split('|')
            hand = list(filter(lambda x: len(x) > 0, hand.strip().split(' ')))
            winning = list(filter(lambda x: len(x) > 0, winning.strip().split(' ')))
            winning = set(winning)
            matched = 0
            for num in hand:
                if num in winning:
                    matched += 1
            matches.append(matched)

    cards_created = [1 for _ in range(len(matches))]
    for i in range(len(cards_created)-2, -1, -1):
        for match in range(1, matches[i]+1):
            cards_created[i] += cards_created[i+match]
    
    print(sum(cards_created))
