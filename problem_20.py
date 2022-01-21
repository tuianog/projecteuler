from functools import reduce

def factorial_recursion(n):
    if n == 1:
        return n
    return n * factorial_recursion(n-1)


def factorial_iterative(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s

def sum_digits(value):
    value_str = str(value)
    value_digits = [int(i) for i in list(value_str)]
    s = reduce(lambda t, x: t+x, value_digits, 0)
    return s

if __name__ == "__main__":
    n = 100
    f = factorial_recursion(n)
    s = sum_digits(f)
    print(f, s)