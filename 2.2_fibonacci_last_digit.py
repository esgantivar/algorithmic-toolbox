def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c % 10


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
