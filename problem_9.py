import math

def find_pythagorean_triplet(value):
    #3+4+5 = 12
    #a^2 + b^2 = c^2
    for a in range(1, value-2):
        for b in range(a+1, value-1):
            for c in range(b+1, value):
                if (a+b+c) == value:
                    aux_a = math.pow(a, 2)
                    aux_b = math.pow(b, 2)
                    aux_c = math.pow(c, 2)
                    if aux_a+aux_b == aux_c:
                        return (a,b,c), a*b*c
    return None, None


if __name__ == "__main__":
    print(find_pythagorean_triplet(1000))