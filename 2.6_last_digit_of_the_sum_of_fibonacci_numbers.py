def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_fast(n):
    if n <= 1:
        return n
    lesser = (n + 2) % 60
    if lesser == 1:
        return 0
    elif lesser == 0:
        return 9
    else:
        f = fibo(lesser)
        if f != 0:
            return f - 1
        else:
            return 9


def fibo(n):
    a, b, c = 0, 1, 0
    for _ in range(2, n + 1):
        c = a + b
        c = c % 10
        b, a = c, b
    return c


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n))
