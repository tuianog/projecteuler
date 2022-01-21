import math
from functools import reduce

def get_power_digit_sum(value, power):
    value = int(math.pow(value, power))
    value_str = str(value)
    value_digits = [int(i) for i in list(value_str)]
    s = reduce(lambda t, x: t+x, value_digits, 0)
    return s

if __name__ == "__main__":
    print(get_power_digit_sum(value=2, power=1000))