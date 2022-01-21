
def get_next_number(n):
    if n%2==0:
        return int(n/2)
    return 3*n+1


def build_sequence(n):
    sequence = [n]
    v = n
    while True:
        v = get_next_number(v)
        sequence.append(v)
        if v == 1:
            return sequence

def find_first_longest_chain(max_n):
    max = 0
    max_value = None
    for i in range(max_n, 1, -1):
        s = len(build_sequence(i))
        if s > max:
            max = s
            max_value = i
    return max, max_value


if __name__ == "__main__":
    #print(build_sequence(13))
    print(find_first_longest_chain(max_n=1000000))