def optimal_points(segments, n):
    index = 0
    coordinates = []

    while index < n:
        curr = lst[index]
        while index < n - 1 and curr[1] >= lst[index + 1][0]:
            index += 1
        coordinates.append(curr[1])
        index += 1
    return coordinates


if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append([int(i) for i in input().split()])
    lst.sort(key=lambda x: x[1])
    coords = optimal_points(lst, n)
    print(len(coords))
    print(' '.join([str(i) for i in coords]))
