
def is_divisible_by(n, values):
    for value in values:
        if n%value != 0:
            return False
    return True

def find_smallest_divisible(v_min, v_max):
    values = [i for i in range(v_max, v_min-1, -1)]
    i = v_max+1
    while True:
        if is_divisible_by(i, values):
            return i
        i += 1


if __name__ == "__main__":
    value = find_smallest_divisible(1, 10)
    print(value)
    
    
        


