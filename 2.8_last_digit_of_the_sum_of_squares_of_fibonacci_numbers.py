# https://math.stackexchange.com/questions/442459/for-the-fibonacci-numbers-show-for-all-n-f-12f-22-dotsf-n2-f-nf-n1
def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    sum = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_fast(n):
    lesser_n = n % 60
    lesser_nplus = (n + 1) % 60
    if lesser_n <= 1:
        a = lesser_n
    else:
        a = fibo(lesser_n)
    if lesser_nplus <= 1:
        b = lesser_nplus
    else:
        b = fibo(lesser_nplus)
    return (a * b) % 10


def fibo(n):
    a, b, c = 0, 1, 0
    for _ in range(2, n + 1):
        c = a + b
        c = c % 10
        b, a = c, b
    return c


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares_fast(n))
