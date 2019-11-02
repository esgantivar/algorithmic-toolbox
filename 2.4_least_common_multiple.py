def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm_fast(a, b):
    if b == 0:
        return a
    c = a % b
    return lcm_fast(b, c)


if __name__ == '__main__':
    a, b = [int(i) for i in input().split()]
    print((a * b) // lcm_fast(a, b))
    print((a * b) // lcm_naive(a, b))
