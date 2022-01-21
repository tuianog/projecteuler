
def get_sum_of_squares(v_min, v_max):
    values = [i for i in range(v_min, v_max+1)]
    s = 0
    for value in values:
        s += value*value
    return s

def get_square_of_sum(v_min, v_max):
    values = [i for i in range(v_min, v_max+1)]
    s = 0
    for value in values:
        s += value
    return s*s


if __name__ == "__main__":
    sum_of_squares = get_sum_of_squares(1, 100)
    square_of_sums = get_square_of_sum(1, 100)
    diff = square_of_sums - sum_of_squares
    print(sum_of_squares, square_of_sums, diff)