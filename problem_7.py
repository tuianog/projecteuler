from utils.prime_factors import is_prime_efficient

def find_max_prime_number(n_max):
    i = 0
    c = 0
    while c < n_max:
        i += 1
        if is_prime_efficient(i):
            c += 1
    return i

if __name__ == "__main__":
    max_prim_number = 10001
    value = find_max_prime_number(max_prim_number)
    print(value)
