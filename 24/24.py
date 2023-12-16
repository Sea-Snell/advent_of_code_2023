
if __name__ == "__main__":
    all_symbols, all_counts = [], []
    with open('24.txt', 'r') as f:
        for line in f:
            symbols, counts = line.strip().split(' ')
            symbols = symbols.strip()
            counts = list(map(int, counts.strip().split(',')))
            all_symbols.append(symbols)
            all_counts.append(counts)

    ans_total = 0
    for symbols, counts in zip(all_symbols, all_counts):
        symbols = '?'.join([symbols]*5)
        counts = counts*5
        memo_table = [[None for _ in range(len(counts)+1)] for _ in range(len(symbols)+1)]

        for start_symbol_idx in range(len(symbols)-1, -1, -1):
            if all(map(lambda x: x == '.' or x == '?', symbols[start_symbol_idx:])):
                memo_table[start_symbol_idx][len(counts)] = 1
            else:
                memo_table[start_symbol_idx][len(counts)] = 0
        
        for start_count_idx in range(len(counts)-1, -1, -1):
            memo_table[len(symbols)][start_count_idx] = 0
        
        segment_has_period = [[False for _ in range(len(symbols)+1)] for _ in range(len(symbols))]
        segment_has_hashtag = [[False for _ in range(len(symbols)+1)] for _ in range(len(symbols))]
        for start_symbol_idx in range(len(symbols)):
            has_period, has_hashtag = False, False
            for end_symbol_idx in range(start_symbol_idx+1, len(symbols)+1):
                if symbols[end_symbol_idx-1] == '.':
                    has_period = True
                if symbols[end_symbol_idx-1] == '#':
                    has_hashtag = True
                segment_has_period[start_symbol_idx][end_symbol_idx] = has_period
                segment_has_hashtag[start_symbol_idx][end_symbol_idx] = has_hashtag
        
        memo_table[-1][-1] = 1

        for start_symbol_idx in range(len(symbols)-1, -1, -1):
            count_total = 0
            for start_count_idx in range(len(counts)-1, -1, -1):
                curr_counts_len = len(counts)-start_count_idx
                curr_symbols_len = len(symbols)-start_symbol_idx
                curr_count = counts[start_count_idx]
                count_total += curr_count

                if (count_total + (curr_counts_len-1)) > curr_symbols_len:
                    memo_table[start_symbol_idx][start_count_idx] = 0
                    continue

                if symbols[start_symbol_idx] == '.':
                    memo_table[start_symbol_idx][start_count_idx] = 0
                    continue
                
                if curr_count > curr_symbols_len:
                    memo_table[start_symbol_idx][start_count_idx] = 0
                    continue
                
                if segment_has_period[start_symbol_idx][start_symbol_idx+curr_count]:
                    memo_table[start_symbol_idx][start_count_idx] = 0
                    continue
                
                if curr_count == curr_symbols_len:
                    memo_table[start_symbol_idx][start_count_idx] = 1
                    continue

                if start_count_idx == len(counts)-1:
                    if not segment_has_hashtag[start_symbol_idx+curr_count][-1]:
                        memo_table[start_symbol_idx][start_count_idx] = 1
                        continue
                    else:
                        memo_table[start_symbol_idx][start_count_idx] = 0
                        continue
                
                total_count = 0
                for end_symbol_idx in range(curr_count+1, curr_symbols_len+1):
                    if symbols[(start_symbol_idx+end_symbol_idx)-1] == '#':
                        break
                    total_count += memo_table[start_symbol_idx+end_symbol_idx][start_count_idx+1]
                
                memo_table[start_symbol_idx][start_count_idx] = total_count

        ans = 0
        for start_symbol_idx in range(len(symbols)):
            ans += memo_table[start_symbol_idx][0]
            if symbols[start_symbol_idx] == '#':
                break
        ans_total += ans
    
    print(ans_total)
