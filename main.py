
def soe(s):
    numbers = [i for i in range(2, s + 1)]
    prime = []
    for j in range(0, len(numbers) + 1):
        prime.append(numbers[j])
        if numbers[j] ^ 2 <= s:
            del numbers[0]
            for k in range(0, len(numbers) + 1):
                if numbers[k] % j == 0:
                    numbers.remove(k)
        else:
            return prime
    print(numbers)
    print(prime)
    return None


n = int(input('Enter limit..'))

prime_numbers = soe(n)
print(prime_numbers)
