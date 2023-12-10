from collections import Counter

def get_hand_class(hand):
    assert len(hand) == 5
    card_counts = Counter(hand)
    sorted_card_counts = card_counts.most_common()
    if sorted_card_counts[0][1] == 5:
        return 0
    if sorted_card_counts[0][1] == 4:
        return 1
    if sorted_card_counts[0][1] == 3 and sorted_card_counts[1][1] == 2:
        return 2
    if sorted_card_counts[0][1] == 3 and sorted_card_counts[1][1] == 1:
        return 3
    if sorted_card_counts[0][1] == 2 and sorted_card_counts[1][1] == 2:
        return 4
    if sorted_card_counts[0][1] == 2 and sorted_card_counts[1][1] == 1:
        return 5
    if sorted_card_counts[0][1] == 1:
        return 6

if __name__ == "__main__":
    with open('13.txt', 'r') as f:
        hands, bids = [], []
        for line in f:
            hand, bid = list(map(lambda x: x.strip(), line.strip().split(' ')))
            hands.append(hand)
            bids.append(int(bid))


    card_rank = {card: idx for idx, card in enumerate('AKQJT98765432')}
    
    hand_classes = [get_hand_class(hand) for hand in hands]
    hand_idxs = [tuple(card_rank[card] for card in hand) for hand in hands]
    total_hand_odering = [(hand_class,)+hand_idx for hand_class, hand_idx in zip(hand_classes, hand_idxs)]
    hand_ordering = list(map(lambda x: x[0], sorted(enumerate(total_hand_odering), key=lambda x: x[1])))
    
    total = 0
    for hand_order, hand_rank in zip(hand_ordering, range(len(hands), 0, -1)):
        bid = bids[hand_order]
        total += bid * hand_rank
    print(total)
