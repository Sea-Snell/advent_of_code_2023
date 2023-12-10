import math

if __name__ == "__main__":
    with open('11.txt', 'r') as f:
        times = list(map(int, filter(lambda x: len(x) > 0, f.readline().split(':')[1].strip().split(' '))))
        distances = list(map(int, filter(lambda x: len(x) > 0, f.readline().split(':')[1].strip().split(' '))))
    
    total_ways = 1
    for t, d in zip(times, distances):
        intersect1 = (t + math.sqrt(t**2-4*d)) / 2
        intersect2 = (t - math.sqrt(t**2-4*d)) / 2
        if intersect1 == math.floor(intersect1):
            intersect1 -= 1
        if intersect2 == math.ceil(intersect2):
            intersect2 += 1
        intersect1 = math.floor(intersect1)
        intersect2 = math.ceil(intersect2)
        delta = (intersect1-intersect2+1)
        total_ways *= delta
    print(total_ways)
