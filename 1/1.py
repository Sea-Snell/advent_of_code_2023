
def main(x):
    total = 0
    for i in range(len(x)):
        first_digit, last_digit = None, None
        for c in x[i]:
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
    with open('1.txt', 'r') as f:
        for line in f:
            x.append(line.strip())
    print(main(x))
