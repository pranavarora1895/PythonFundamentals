def calc_prime(number):
    flag = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            flag += 1
    return flag < 2


def is_prime(number):
    check_prime = calc_prime(number)
    print(check_prime)


def print_prime(interval):
    for counter in range(2, interval + 1):
        check_prime = calc_prime(counter)
        if check_prime:
            print(counter)