def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a, b):
    if b == 0:
        return a
    c = a % b
    return gcd_fast(b, c)


if __name__ == '__main__':
    n1, n2 = [int(i) for i in input().split()]
    print(f'fast: {gcd_fast(n1, n2)}, naive: {gcd_naive(n1, n2)}')
