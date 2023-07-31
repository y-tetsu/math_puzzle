"""Q63
"""
import datetime


def solve():
    """解答
    """
    q = q63()
    area = 0
    for y in range(2006, 2015 + 1):
        for m in range(1, 12 + 1):
            area += q.search(y, m)
    print(area)


class q63:
    def __init__(self):
        self.holiday = self.get_holiday('q63.txt')
        self.one_day = datetime.timedelta(days=1)
        self.one_week = datetime.timedelta(days=7)

    def get_holiday(self, filename):
        """休日を記憶
        """
        ret = {}
        with open(filename, 'r') as fin:
            for line in fin.readlines():
                ret[line.strip()] = True
        return ret

    def search(self, year, month):
        """指定月の最大面積を返す
        """
        day = datetime.date(year, month, 1)
        max_area_month = 0
        max_date = ''
        while day.month == month:
            if self.is_weekday(day):
                max_length = 0
                day_l = day
                while day_l.month == month and self.is_weekday(day_l):
                    day_l += self.one_day
                    max_length += 1
                max_width = 0
                day_w = day
                while day_w.month == month and self.is_weekday(day_w):
                    day_w += self.one_week
                    max_width += 1
                max_area_day = 0
                for width in range(max_width):
                    for length in range(max_length):
                        area = self.get_max_area(length + 1, width + 1, day)
                        if area > max_area_day:
                            max_area_day = area
                if max_area_day > max_area_month:
                    max_area_month = max_area_day
                    max_date = day.strftime('%Y/%m/%d')
            day += self.one_day
        print(max_date, max_area_month)
        return max_area_month

    def get_max_area(self, length, width, day):
        """指定日の最大面積を返す
        """
        area = 0
        day_w = day
        for _ in range(width):
            day_check = day_w
            for _ in range(length):
                if day_check.month != day.month or not self.is_weekday(day_check):
                    return 0
                area += 1
                day_check += self.one_day
            day_w += self.one_week
        return area

    def is_weekday(self, day):
        """平日かどうかを返す
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        date_text = day.strftime('%Y/%m/%d')
        if date_text in self.holiday:
            return False
        return True


if __name__ == '__main__':
    solve()
