from datetime import date, time, datetime, timedelta

def date_of(weekday, incidence, month_within):
    current_month = month_within.replace(day=1)
    shift = (weekday - current_month.weekday()) % 7
    return current_month + timedelta(days=shift, weeks=incidence)

def next_date(weekday, incidence, after = None):
    if after is None:
        after = date.today()
    this_month = date_of(weekday, incidence, after)
    if this_month > after:
        return this_month
    else:
        return date_of(weekday, incidence, after.replace(day=28) + timedelta(days=4))


nights = [
    ('SyPy', 0, 3, time(18)),
    ('Hacknight', 2, 1, time(18)),
    ('SyDjango', 3, 3, time(18))
]

upcoming = sorted((next_date(weekday, incidence), time, event) for event, incidence, weekday, time in nights)
for date, time, event in upcoming:
    print("Next %s:\t%s" % (event, datetime.combine(date, time)))
