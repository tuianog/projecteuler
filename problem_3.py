import math

def find_max_prime_factor(n):
    while n%2 == 0:
        n = n/2
    
    max_prime_factor = 2
    for i in range(3, int(math.sqrt(n)), 2):
        while n%i == 0:
            max_prime_factor = i
            n = n/i
    return max_prime_factor
    

if __name__ == "__main__":
    max_prime_factor = find_max_prime_factor(600851475143)
    print(max_prime_factor)