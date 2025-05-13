def is_leap_year(year):
    Leap = True
    if year % 4 == 0:
        if year % 100 == 0:
            Leap = False
        if year % 400 == 0:
            Leap = True
    else:
        Leap = False
    return Leap
print(is_leap_year(2024))