import random

def quicksort(values):
    if not len(values):
        return values
    pivot = random.choice(values)

    same, lower, bigger = [], [], []
    for value in values:
        if value == pivot:
            same.append(value)
        elif value < pivot:
            lower.append(value)
        else:
            bigger.append(value)
    
    sorted_lower = quicksort(lower)
    sorted_bigger = quicksort(bigger)
    return sorted_lower + same + sorted_bigger


def bublesort(values):
    for i in range(len(values)):
        for j in range(0, i):
            if values[j] > values[i]:
                tmp = values[i]
                values[i] = values[j]
                values[j] = tmp
    return values


if __name__ == "__main__":
    values = [4,2,2,6,1, 2]
    print(quicksort(values))
    print(bublesort(values))
