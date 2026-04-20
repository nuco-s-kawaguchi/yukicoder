def is_prime_number(number):
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2

    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2

    return True


def generate_primes(number):
    primes = []
    for i in range(2, number + 1):
        if is_prime_number(i):
            primes.append(i)
    return primes


def main():
    number = int(input())

    primes = generate_primes(number)

    dp = [False] * (number + 1)

    for i in range(2, number + 1):
        dp[i] = False

        for p in primes:
            if p > i:
                break

            next_value = i - p

            if next_value >= 2 and not dp[next_value]:
                dp[i] = True
                break

    print("Win" if dp[number] else "Lose")


if __name__ == "__main__":
    main()
