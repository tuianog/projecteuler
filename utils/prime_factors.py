import math

def is_prime(n):
    # filter if even and greater than 2
    if n > 2 and n % 2 == 0:
        return False

    factors = []
    for i in range(2, int(n/2)):
        if n%i == 0:
            factors.append(i)
    return len(factors) == 0


def is_prime_efficient(n):
    if n <= 1:
        return False
    
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def find_prime_factors(n):
    while n%2 == 0:
        n = n/2

    factors = []
    for i in range(3, int(math.sqrt(n)), 2):
        while n%i == 0:
            factors.append(i)
            n = n/i
    return factors

if __name__ == "__main__":
    factors = find_prime_factors(4)
    print(factors)