import math


def compute_min_refills(distance, tank, stops):
    len_stops = len(stops)
    before = 0
    count = 0
    for i in range(len_stops):
        next_idx = i + 1
        curr_mile, next_mile = stops[i], math.inf
        if next_idx < len_stops:
            next_mile = stops[next_idx]
        if (before + tank) < next_mile:
            if distance >= (before + tank) >= curr_mile:
                before = curr_mile
                count += 1
    return count if (before + tank) >= distance else -1


if __name__ == '__main__':
    d = int(input())  # miles to travel
    m = int(input())  # miles to tank
    n = int(input())  # number of stops

    stops = [int(i) for i in input().split()]

    print(compute_min_refills(d, m, stops))
