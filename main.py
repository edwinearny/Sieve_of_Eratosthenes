
def soe(s):
    numbers = [i for i in range(2, s + 1)]
    prime = []
    composite = []
    for j in numbers:
        if j in composite:
            continue
        prime.append(j)
        if j ** 2 <= s:
            for k in range(numbers[j] - 2, len(numbers)):
                if numbers[k] % j == 0:
                    composite.append(numbers[k])
        else:
            break

    buffer = list(set(numbers) - set(composite))
    buffer = list(set(buffer) - set(prime))
    prime = prime + buffer
    return prime


n = int(input('Enter limit..'))

prime_numbers = soe(n)
print(f'Primes till {n} are {prime_numbers}')
