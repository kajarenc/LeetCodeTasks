# https://leetcode.com/problems/day-of-the-year


def dayOfYear(date: str) -> int:
    year, month, day = date.split('-')

    year, month, day = int(year), int(month), int(day)

    extra_day = False
    if year % 400 == 0:
        extra_day = True
    elif year % 100 == 0:
        extra_day = False
    elif year % 4 == 0:
        extra_day = True

    months = {1: 31,
              2: 28,
              3: 31,
              4: 30,
              5: 31,
              6: 30,
              7: 31,
              8: 31,
              9: 30,
              10: 31,
              11: 30,
              12: 31,
              }

    result = 0

    for i in range(1, month):
        result += months[i]

    result += day

    if extra_day and month >= 3:
        result += 1
    return result
