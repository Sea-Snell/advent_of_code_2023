import sys
sys.setrecursionlimit(100000)
from collections import defaultdict

if __name__ == "__main__":
    with open('32.txt', 'r') as f:
        grid = [line.strip() for line in f]
    
    initial_nodes = []
    for i in range(len(grid)):
        initial_nodes.append((i, 0, 0, 1))
        initial_nodes.append((i, len(grid[i])-1, 0, -1))
    for i in range(len(grid[0])):
        initial_nodes.append((0, i, 1, 0))
        initial_nodes.append((len(grid)-1, i, -1, 0))

    visited, node_stack = defaultdict(lambda: set()), list(initial_nodes)

    transform_check = lambda i: i[0] >= 0 and i[1] >= 0 and i[0] < len(grid) and i[1] < len(grid[i[0]]) and (i[2]+i[3]) != 0 and (i[2]*i[3]) == 0

    transforms = {
        '.': lambda y, x, dy, dx: list(filter(transform_check, [(y+dy, x+dx, dy, dx)])),
        '/': lambda y, x, dy, dx: list(filter(transform_check, [(y-dx, x-dy, -dx, -dy)])),
        '\\': lambda y, x, dy, dx: list(filter(transform_check, [(y+dx, x+dy, dx, dy)])),
        '-': lambda y, x, dy, dx: list(filter(transform_check, [(y, x+min(dx+1, 1), 0, min(dx+1, 1)), (y, x+max(dx-1, -1), 0, max(dx-1, -1))])),
        '|': lambda y, x, dy, dx: list(filter(transform_check, [(y+min(dy+1, 1), x, min(dy+1, 1), 0), (y+max(dy-1, -1), x, max(dy-1, -1), 0)])),
    }

    def recur(node, path=None):
        if path is None:
            path = set([node])
        assert node in path
        y, x, dy, dx = node
        if isinstance(visited[(y, x, dy, dx)], set) and len(visited[(y, x, dy, dx)]) == 0:
            curr_back_references = set()
            curr_visits = set([(y, x, dy, dx)])
            for transform in transforms[grid[y][x]](y, x, dy, dx):
                if transform in path:
                    curr_back_references.add(transform)
                else:
                    transform_visits, transform_back_references = recur(transform, path | set([transform]))
                    curr_back_references.update(transform_back_references)
                    curr_visits.update(transform_visits)
            if (y, x, dy, dx) in curr_back_references:
                curr_back_references.remove((y, x, dy, dx))
                if len(curr_back_references) == 0:
                    for item in curr_visits:
                        if isinstance(visited[item], tuple):
                            visited[item] = curr_visits
            if len(curr_back_references) > 0:
                visited[(y, x, dy, dx)] = next(iter(curr_back_references))
            else:
                visited[(y, x, dy, dx)] = curr_visits
            return curr_visits, curr_back_references
        elif isinstance(visited[y, x, dy, dx], tuple):
            v = visited[y, x, dy, dx]
            while isinstance(visited[v], tuple):
                v = visited[v]
            assert v in path
            return set(), set([v])
        elif isinstance(visited[(y, x, dy, dx)], set) and len(visited[(y, x, dy, dx)]) > 0:
            return visited[(y, x, dy, dx)], set()
        else:
            raise NotImplementedError

    for node in initial_nodes:
        recur(node)
    
    largest_size = 0
    for node in initial_nodes:
        largest_size = max(largest_size, len(set([(y, x) for y, x, _, _ in visited[node]])))

    print(largest_size)
