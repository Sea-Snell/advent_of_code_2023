import math
from collections import defaultdict

# NOTE: this one is a bit hacked together and is not quite a fully general solution

def primes_less_than(n):
    primes = []
    if n > 2:
        primes.append(2)
    for i in range(3, n, 2):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
            if prime*prime > i:
                break
        if is_prime:
            primes.append(i)
    return primes

def prime_factors(n):
    primes = primes_less_than(int(math.sqrt(n))+1)
    prime_factors = defaultdict(int)
    for prime in primes:
        while n % prime == 0:
            prime_factors[prime] += 1
            n //= prime
        if n == 1:
            break
    if n != 1:
        prime_factors[n] += 1
    return prime_factors

def lcm(a, b):
    a_prime_factors = prime_factors(a)
    b_prime_factors = prime_factors(b)
    lcm_prime_factors = defaultdict(int)
    for factor in set(b_prime_factors.keys()).union(set(a_prime_factors.keys())):
        lcm_prime_factors[factor] = max(a_prime_factors[factor], b_prime_factors[factor])
    lcm = 1
    for factor, power in lcm_prime_factors.items():
        lcm *= factor**power
    return lcm

if __name__ == "__main__":
    with open('16.txt', 'r') as f:
        instructions = [0 if inst == 'L' else 1 for inst in f.readline().strip()]
        _ = f.readline()
        graph = {}
        for line in f:
            node, connections = line.split(' = ')
            node = node.strip()
            l_connection, r_connection = connections.strip().split(', ')
            l_connection = l_connection[1:]
            r_connection = r_connection[:-1]
            graph[node] = (l_connection, r_connection)
        
    connection_from_each_start_node = {}
    for start_node in graph.keys():
        curr_node = start_node
        for instruction in instructions:
            curr_node = graph[curr_node][instruction]
        connection_from_each_start_node[start_node] = curr_node

    start_nodes = [node for node in graph.keys() if node[-1] == 'A']

    loop_start_idxs, loop_sizes, initial_end_node_visits, loop_end_node_visits = [], [], [], []
    for start_node in start_nodes:
        visited_nodes = dict()
        curr_node = start_node
        end_node_idxs = []
        while not (curr_node in visited_nodes):
            if curr_node[-1] == 'Z':
                end_node_idxs.append(len(visited_nodes))
            visited_nodes[curr_node] = len(visited_nodes)
            curr_node = connection_from_each_start_node[curr_node]

        loop_start_idx = visited_nodes[curr_node]
        loop_size = len(visited_nodes) - loop_start_idx
        initial_end_node_visit = set(filter(lambda x: x < loop_start_idx, end_node_idxs))
        loop_end_node_visit = set(map(lambda x: x - loop_start_idx, filter(lambda x: x >= loop_start_idx, end_node_idxs)))
        loop_start_idxs.append(loop_start_idx)
        loop_sizes.append(loop_size)
        initial_end_node_visits.append(initial_end_node_visit)
        loop_end_node_visits.append(loop_end_node_visit)
    
    print(loop_start_idxs, loop_sizes, initial_end_node_visits, loop_end_node_visits)
    
    # loop_start_idx = 1
    # loop_sizes = [73, 67, 79, 61, 43, 53]
    # loop_mods = [72, 66, 78, 60, 42, 52]

    # lcm_mod = 1
    # for loop_size in loop_sizes:
    #     lcm_mod *= loop_size
    
    # curr_mod, curr_size = loop_mods[0], loop_sizes[0]
    # for mod, loop_size in zip(loop_mods[1:], loop_sizes[1:]):
    #     mod_inverse = 0
    #     while (curr_size * mod_inverse) % loop_size != 1:
    #         mod_inverse += 1

    #     x = ((mod - curr_mod) * mod_inverse) % loop_size
    #     curr_mod = (curr_size * x + curr_mod) % (curr_size * loop_size)
    #     curr_size = curr_size * loop_size

    # print((curr_mod+loop_start_idx)*len(instructions))

    max_initial_steps = max(loop_start_idxs)
    terminal_step = None
    for step in range(max_initial_steps):
        has_end_node = []
        for node_idx in range(len(start_nodes)):
            if step < loop_start_idxs[node_idx]:
                if step in initial_end_node_visits[node_idx]:
                    has_end_node.append(True)
                else:
                    has_end_node.append(False)
            else:
                loop_position = (step - loop_start_idxs[node_idx]) % loop_sizes[node_idx]
                if loop_position in loop_end_node_visits[node_idx]:
                    has_end_node.append(True)
                else:
                    has_end_node.append(False)
        if all(has_end_node):
            terminal_step = step
            break

    if terminal_step is not None:
        print(terminal_step*len(instructions))
    else:
        modulos = []
        for node_idx in range(len(start_nodes)):
            assert len(loop_end_node_visits[node_idx]) == 1, 'not implemented'
            loop_end_node_visit = loop_end_node_visits[node_idx].pop()
            loop_position = (max_initial_steps - loop_start_idxs[node_idx]) % loop_sizes[node_idx]
            loop_mod = (loop_end_node_visit - loop_position) % loop_sizes[node_idx]
            modulos.append(loop_mod)

        curr_mod, curr_size = 0, 1
        for modulo, loop_size in zip(modulos, loop_sizes):
            # curr_size * x + curr_mod == modulo (mod loop_size)
            # x == (modulo - curr_mod) / curr_size (mod loop_size)
            mod_inverse = 0
            while (curr_size * mod_inverse) % loop_size != 1:
                mod_inverse += 1
            
            x = ((modulo - curr_mod) * mod_inverse) % loop_size
            new_curr_size = lcm(loop_size, curr_size)
            curr_mod = (curr_size * x + curr_mod) % new_curr_size
            curr_size = new_curr_size

        print((max_initial_steps+curr_mod)*len(instructions))
