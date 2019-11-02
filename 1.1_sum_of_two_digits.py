def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    print('type numbers')
    a, b = [int(i) for i in input().split()]
    print(sum_of_two_digits(a, b))
