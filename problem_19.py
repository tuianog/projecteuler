
days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

months = [
    ("january", 31),
    ("february", 28), # changed when leap year
    ("march", 31),
    ("april", 30),
    ("may", 31),
    ("june", 30),
    ("july", 31),
    ("august", 31),
    ("september", 30),
    ("october", 31),
    ("november", 30),
    ("december", 31)
]

def is_leap_year(year):
    if year%100!=0:
        if year%4==0:
            return True
    else:
        if year%400==0:
            return True
    return False

def determine_start_day_position(target_year, target_day, target_month):
    # 1 Jan 1900 was a Monday
    year = 1900
    day_position = 1 # monday
    while year <= target_year:
        month = 1
        if is_leap_year(year):
            # change february max days
            months[1] = (months[1][0], 29)
        else:
            months[1] = (months[1][0], 28)
        
        while month <= len(months):
            month_max_days = months[month-1][1]
            day = 1
            while day <= month_max_days:
                if year == target_year and month == target_month and day == target_day:
                    return days[day_position], day_position
                if (day_position+1) % len(days) == 0:
                    day_position = 0
                else:
                    day_position += 1
                day += 1
            month += 1
        year += 1
    return None

def search_days(start_year, end_year, start_day_position, day_to_count):
    c = 0
    i = start_day_position
    for year in range(start_year, end_year+1):
        if is_leap_year(year):
            # change february max days
            months[1] = (months[1][0], 29)
        else:
            months[1] = (months[1][0], 28)
        
        for _month, max_days in months:
            n_days = 0
            while n_days < max_days:
                day = days[i]
                if n_days == 0 and day == day_to_count:
                    c += 1
                if (i+1) % len(days) == 0:
                    i = 0
                else:
                    i += 1
                n_days += 1
    return c


if __name__ == "__main__":
    # starts on a monday
    start_year = 1901
    start_position_day, start_position = determine_start_day_position(target_year=start_year, target_day=1, target_month=1)
    #print(start_position_day)
    v = search_days(start_year=start_year, end_year=2000, start_day_position=start_position, day_to_count="sunday")
    print(v)
