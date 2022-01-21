

def fibonacci_recursion(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)


def fibonacci_iterative(n, max_value=4000000):
    fib = [1, 2]
    for i in range(2, n):
        value = fib[i-2]+fib[i-1]
        fib.append(value)
        if value > max_value:
            fib.pop()
            return fib
    return fib


def find_sum_even(values):
    s = 0
    for value in values:
        if value %2 == 0:
            s+=value
    return s

if __name__ == "__main__":
    sequence = fibonacci_iterative(2000)
    total = find_sum_even(sequence)
    print(sequence)
    print(total)