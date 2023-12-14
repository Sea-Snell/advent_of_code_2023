
if __name__ == "__main__":
    all_symbols, all_counts = [], []
    with open('23.txt', 'r') as f:
        for line in f:
            symbols, counts = line.strip().split(' ')
            symbols = symbols.strip()
            counts = list(map(int, counts.strip().split(',')))
            all_symbols.append(symbols)
            all_counts.append(counts)

    ans_total = 0
    for symbols, counts in zip(all_symbols, all_counts):
        memo_table = [[None for _ in range(len(counts)+1)] for _ in range(len(symbols)+1)]

        for start_symbol_idx in range(len(symbols)-1, -1, -1):
            if all(map(lambda x: x == '.' or x == '?', symbols[start_symbol_idx:])):
                memo_table[start_symbol_idx][len(counts)] = 1
            else:
                memo_table[start_symbol_idx][len(counts)] = 0
        
        for start_count_idx in range(len(counts)-1, -1, -1):
            memo_table[len(symbols)][start_count_idx] = 0
        
        memo_table[-1][-1] = 1

        for start_symbol_idx in range(len(symbols)-1, -1, -1):
            for start_count_idx in range(len(counts)-1, -1, -1):
                curr_symbols = symbols[start_symbol_idx:]
                curr_counts = counts[start_count_idx:]

                if (sum(curr_counts) + (len(curr_counts)-1)) > len(curr_symbols):
                    memo_table[start_symbol_idx][start_count_idx] = 0
                    continue

                if symbols[start_symbol_idx] == '.':
                    memo_table[start_symbol_idx][start_count_idx] = 0
                    continue
                
                curr_count = counts[start_count_idx]
                if curr_count > len(curr_symbols):
                    memo_table[start_symbol_idx][start_count_idx] = 0
                    continue

                current_segment = curr_symbols[:curr_count]
                if not all(map(lambda x: x == '#' or x == '?', current_segment)):
                    memo_table[start_symbol_idx][start_count_idx] = 0
                    continue
                
                if curr_count == len(curr_symbols):
                    memo_table[start_symbol_idx][start_count_idx] = 1
                    continue

                if start_count_idx == len(counts)-1:
                    if all(map(lambda x: x == '.' or x == '?', curr_symbols[curr_count:])):
                        memo_table[start_symbol_idx][start_count_idx] = 1
                        continue
                    else:
                        memo_table[start_symbol_idx][start_count_idx] = 0
                        continue
                
                total_count = 0
                for end_symbol_idx in range(curr_count+1, len(curr_symbols)+1):
                    current_suffix = curr_symbols[curr_count:end_symbol_idx]
                    if all(map(lambda x: x == '.' or x == '?', current_suffix)):
                        total_count += memo_table[start_symbol_idx+end_symbol_idx][start_count_idx+1]
                
                memo_table[start_symbol_idx][start_count_idx] = total_count
        

        ans = 0
        for start_symbol_idx in range(len(symbols)):
            ans += memo_table[start_symbol_idx][0]
            if symbols[start_symbol_idx] == '#':
                break
        ans_total += ans
    
    print(ans_total)
