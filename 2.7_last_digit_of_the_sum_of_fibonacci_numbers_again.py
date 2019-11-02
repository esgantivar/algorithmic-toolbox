def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_fast(m, n):
    if n <= 1:
        return n

    lesser_n = (n + 2) % 60
    lesser_m = (m + 1) % 60

    if lesser_n <= 1:
        a = lesser_n - 1
    else:
        a = fibo(lesser_n)
    if lesser_m <= 1:
        b = lesser_m - 1
    else:
        b = fibo(lesser_m)
    if a >= b:
        return (a - b) % 10
    else:
        return 10 + a - b


def fibo(n):
    a, b, c = 0, 1, 0
    for _ in range(2, n + 1):
        c = a + b
        c = c % 10
        b, a = c, b
    return c


if __name__ == '__main__':
    m, n = [int(i) for i in input().split()]
    print(fibonacci_partial_sum_naive(m, n))
    print(fibonacci_partial_sum_fast(m, n))
