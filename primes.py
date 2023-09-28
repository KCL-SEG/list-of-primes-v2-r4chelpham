import math
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""




def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError('Not a positive value')
    list = []

    def check_prime(n):
        prime = 1

        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                prime = 0
                break
            else:
                continue

        return prime

    counter = 0
    n = 2

    while counter < number_of_primes:
        if check_prime(n) == 1:
            list.append(n)
            counter += 1
        n += 1

    return list

print(primes(20))
