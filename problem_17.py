from functools import reduce

mappings_1_digit = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

mappings_2_digits = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety"
}

mappings_3_digits = {
    "100": "hundred"
}

mappings_4_digits = {
    "1000": "thousand"
}

def parse_number_letters(n):
    n_str = str(n)
    if len(n_str) == 1:
        return mappings_1_digit[n_str]
    if len(n_str) == 2:
        if n <= 20 or n_str[-1] == '0':
            return mappings_2_digits[n_str]
        else:
            return f"{mappings_2_digits[f'{n_str[0]}0']}-{mappings_1_digit[n_str[1]]}"
    if len(n_str) == 3:
        hundred_value = mappings_1_digit[n_str[0]]
        if n_str[1:] == '00':
            return f"{hundred_value} hundred"
        new_n = int(n_str[1:])
        return f"{hundred_value} hundred and {parse_number_letters(new_n)}"
    if len(n_str) == 4:
        # only prepared for number 1000
        return f"{mappings_1_digit[n_str[0]]} thousand"

def sum_number_letters(n):
    n_str = parse_number_letters(n)
    n_str_lst = list(filter(lambda x: x not in [' ', '-'], list(n_str)))
    c = reduce(lambda t, _x: t+1, n_str_lst, 0)
    return c, n_str, n_str_lst

def sum_all_number_letters(n_min, n_max):
    s = 0
    for i in range(n_min, n_max+1):
        s += sum_number_letters(i)[0]
    return s

if __name__ == "__main__":
    # print(sum_number_letters(n=342))
    # print(sum_number_letters(n=999))
    # print(sum_number_letters(n=1))
    # print(sum_number_letters(n=1000))
    # print(sum_number_letters(n=115))
    # print(sum_number_letters(n=235))
    # print(sum_number_letters(n=230))
    # print(sum_number_letters(n=590))
    # print(sum_number_letters(n=88))
    #print(sum_number_letters(n=100))
        
    s = sum_all_number_letters(1, 1000)
    print(s)