from datetime import date, timedelta
from collections import defaultdict
import calendar

WHICH_TO_INDEX = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3,
                  '5th': 4, 'last': -1}

class MeetupDayException(Exception):
    pass

def meetup_day(year, month, day_of_the_week, which):
    by_dow = defaultdict(list)
    dt = date(year, month, 1)
    one_day = timedelta(days=1)

    while dt.month == month:
        by_dow[calendar.day_name[dt.weekday()]].append(dt.day)
        dt = dt + one_day

    if which == 'teenth':
        day = [d for d in by_dow[day_of_the_week] if 13 <= d <= 19][0]

    if which in WHICH_TO_INDEX:
        index = WHICH_TO_INDEX[which]
        try:
            day = by_dow[day_of_the_week][index]
        except IndexError:
            raise MeetupDayException("invalid param: 'which'")

    return date(year, month, day)
