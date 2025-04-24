
def soe(s):
    if s < 2:
        return []

    is_prime = [True] * (s + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(s ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, s + 1, i):
                is_prime[j] = False

    prime = [i for i, p in enumerate(is_prime) if p]
    return prime


n = int(input('Enter limit..'))

prime_numbers = soe(n)
print(f'Primes till {n} are {prime_numbers}')
