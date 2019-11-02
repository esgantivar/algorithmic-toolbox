def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    numbers.sort()
    max_1 = numbers.pop()
    if not max_1:
        max_1 = 0
    max_2 = numbers.pop()
    if not max_2:
        max_2 = 0
    return max_1 * max_2


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
