def count_prime_factors(number):
    count = 0
    remaining_number = number

    while remaining_number % 2 == 0:
        count += 1
        remaining_number //= 2

    factor = 3
    while factor * factor <= remaining_number:
        while remaining_number % factor == 0:
            count += 1
            remaining_number //= factor
        factor += 2

    if remaining_number != 1:
        count += 1

    return count


def main():
    number = int(input())
    prime_factor_count = count_prime_factors(number)
    result = "YES" if prime_factor_count >= 3 else "NO"
    print(result)


if __name__ == "__main__":
    main()