def prime_number(N):
    if N < 2:
        return False
    if N % 2 == 0:
        return N == 2
    i = 3
    while i * i <= N:
        if N % i == 0:
            return False
        i += 2
    return True


def generate_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if prime_number(i):
            primes.append(i)
    return primes


def can_first_player_win(N):
    primes = generate_primes(N)
    dp = [False] * (N + 1)
    for i in range(2, N + 1):
        for p in primes:
            if p > i:
                break
            next_value = i - p
            if next_value >= 2 and not dp[next_value]:
                dp[i] = True
                break
    return dp[N]


def main():
    N = int(input())
    print("Win" if can_first_player_win(N) else "Lose")


if __name__ == "__main__":
    main()