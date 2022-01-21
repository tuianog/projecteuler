

def is_number_palindrome(n):
    n_str = str(n)
    if len(n_str) < 2:
        return False
    
    stop_condition = 1 if len(n_str) % 2 == 0 else 2
        
    i, j = 0, len(n_str)-1
    while (j-i) != stop_condition:
        if n_str[i] != n_str[j]:
            return False 
        i += 1
        j -= 1
    return n_str[i] == n_str[j]


def find_max_palindrome_from_product_of_numbers(n_min, n_max):
    mid = int((n_min+n_max)/2)+1
    max = -1
    values = ()
    for i in range(n_min, n_max+1):
        for j in range(n_max, mid-1, -1):
            value = i*j
            if is_number_palindrome(value) and value > max:
                max = value
                values = (i,j)
    return max, values

if __name__ == "__main__":
    print(find_max_palindrome_from_product_of_numbers(100, 999))