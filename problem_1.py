
def problem_1(n=1000):
    s = 0
    for i in range(1, n):
        if i%3 == 0 or i%5==0:
            s += i
    return s

if __name__ == "__main__":
    print(problem_1(1000))