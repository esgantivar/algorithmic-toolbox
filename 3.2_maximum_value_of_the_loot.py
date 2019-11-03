def get_optimal_value(W, items):
    value = 0.
    for v, w in items:
        w_min = min(w, W)
        value += w_min * (v / w)
        W -= w_min
    return value


if __name__ == '__main__':
    n, W = [int(i) for i in input().split()]
    items = []
    for _ in range(n):
        items.append([int(i) for i in input().split()])
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    print(get_optimal_value(W, items))
