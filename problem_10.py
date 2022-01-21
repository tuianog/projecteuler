from utils.prime_factors import is_prime_efficient

def sum_primes(limit):
    s = 0
    for i in range(2, limit+1):
        if is_prime_efficient(i):
            s += i
    return s

if __name__ == "__main__":
    print(sum_primes(2000000))
