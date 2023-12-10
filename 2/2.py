
def is_end_of_word_digit(word, idx):
    word_digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    word = word[:(idx+1)]
    for word_digit in word_digits.keys():
        if word.endswith(word_digit):
            return word_digits[word_digit]
    return None

def main(x):
    total = 0
    for i in range(len(x)):
        first_digit, last_digit = None, None
        for c_idx, c in enumerate(x[i]):
            word_digit = is_end_of_word_digit(x[i], c_idx)
            if word_digit is not None:
                c = word_digit
            if c.isdigit():
                last_digit = c
                if first_digit is None:
                    first_digit = c
        assert (first_digit is not None) and (last_digit is not None)
        num = int(first_digit + last_digit)
        total += num
    return total

if __name__ == "__main__":
    x = []
    with open('2.txt', 'r') as f:
        for line in f:
            x.append(line.strip())
    print(main(x))
