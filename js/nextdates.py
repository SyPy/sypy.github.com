from datetime import datetime
import calendar
import math

now = datetime.now()
def next_date(week, day_of_week):
    year, month = (now.year, now.month)
    day = calendar.monthcalendar(now.year, now.month)[week][day_of_week]
    if now.day > day:
        year = int(2014 + math.floor(11/12))
        month = now.month % 12 + 1
        day = calendar.monthcalendar(year, month)[week][day_of_week]
    return datetime(year, month, day, 18, 30)

nights = [('SyPy', 0, 3), ('Hacknight', 2, 1), ('SyDjango', 3, 3)]
for date, event in sorted([(next_date(week, day), event) for event, week, day in nights]):
    print("Next %s:\t%s" % (event, date))

# developed at hacknight 2014-10-16



