import math

def sum_triangle_numbers(n):
    triangle_numbers = []
    s = 0
    for i in range(1, n+1):
        s += i
        triangle_numbers.append(s)
    return triangle_numbers

def find_divisors(value):
    c = 2 # include 1 and value itself
    v = int(math.sqrt(value))
    for i in range(2, v+1):
        if value%i == 0:
            c += 1
            r = int(value/i)
            if r != i:
                c+= 1
    return c

def find_factors_efficient(value):
    factors = [1]
    c = int(math.sqrt(value))
    for i in range(2, c+1):
        if value%i == 0:
            factors.append(i)
            r = int(value/i)
            if r != i:
                factors.append(r)

    return [*factors, value]

def get_first_triangle_number_with_most_divisors(max_n_divisors):
    s, i = 0, 0
    while True:
        s += i
        if find_divisors(s) >= max_n_divisors:
            return s
        i += 1

if __name__ == "__main__":
    #print(sum_triangle_numbers(12))
    print(get_first_triangle_number_with_most_divisors(500))