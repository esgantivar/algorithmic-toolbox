def get_change(m):
    coins = [10, 5, 1]
    total = 0
    count = 0
    while total != m:
        for c in coins:
            if (m - total) >= c:
                total += c
                count += 1
                break
    return count


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
