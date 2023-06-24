"""Q63
"""
import datetime


def get_holiday(filename):
    """
    休日を記憶
    """
    ret = {}

    with open(filename, 'r') as fin:
        for line in fin.readlines():
            ret[line.strip()] = True

    return ret


def search(year, month):
    """
    指定月の最大面積を返す
    """
    day = datetime.date(year, month, 1)
    max_area_month = 0
    max_date = ''
    while day.month == month:
        if is_weekday(day):
            max_length = 0
            day_l = day

            while day_l.month == month and is_weekday(day_l):
                day_l += ONE_DAY
                max_length += 1

            max_width = 0
            day_w = day

            while day_w.month == month and is_weekday(day_w):
                day_w += ONE_WEEK
                max_width += 1

            max_area_day = 0
            for width in range(max_width):
                for length in range(max_length):
                    area = get_max_area(length + 1, width + 1, day)

                    if area > max_area_day:
                        max_area_day = area

            if max_area_day > max_area_month:
                max_area_month = max_area_day
                max_date = day.strftime('%Y/%m/%d')

        day += ONE_DAY

    print(max_date, max_area_month)

    return max_area_month


def get_max_area(length, width, day):
    """
    指定日の最大面積を返す
    """
    area = 0
    day_w = day

    for _ in range(width):
        day_check = day_w

        for _ in range(length):
            if day_check.month != day.month or not is_weekday(day_check):
                return 0

            area += 1
            day_check += ONE_DAY
        day_w += ONE_WEEK

    return area


def is_weekday(day):
    """
    平日かどうかを返す
    """
    if day.weekday() == 5 or day.weekday() == 6:
        return False

    date_text = day.strftime('%Y/%m/%d')
    if date_text in HOLIDAY:
        return False

    return True


if __name__ == '__main__':
    HOLIDAY = get_holiday('q63.txt')
    ONE_DAY = datetime.timedelta(days=1)
    ONE_WEEK = datetime.timedelta(days=7)
    AREA = 0

    for y in range(2006, 2015 + 1):
        for m in range(1, 12 + 1):
            AREA += search(y, m)

    print("result =", AREA)
