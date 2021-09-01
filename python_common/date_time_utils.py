import datetime
from datetime import timedelta


def get_current_time():
    return datetime.datetime.now().strftime('%H:%M:%S')

def is_day_weekends(date_str):
    date = datetime.date.fromisoformat(date_str)
    weekday_num = datetime.datetime.isoweekday(date)
    if weekday_num < 6:
        return False
    else:
        return True

def calculate_date(date_str, calc_date, skip_weekends):
    date = datetime.date.fromisoformat(date_str) 
    passDays = 0
    if skip_weekends:
        week_ends_count = 0
        work_days_count = 0
        if calc_date < 0:
            while (work_days_count > calc_date) :
                if not is_day_weekends(str(date + timedelta(days=passDays))):
                    work_days_count -= 1
                else : 
                    week_ends_count -= 1
                passDays += 1
        elif calc_date > 0:
            while (work_days_count < calc_date) :
                if not is_day_weekends(str(date + timedelta(days=passDays))):
                    work_days_count += 1
                else :
                    week_ends_count += 1
                passDays += 1

        calc_date += week_ends_count
    return date + timedelta(days=calc_date)

def get_last_day_of_month(date_str) :
    date = datetime.date.fromisoformat(date_str)
    return (date.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)

def get_first_day_of_month(date_str) :
    date = datetime.date.fromisoformat(date_str)
    return date.replace(day=1)

print(get_last_day_of_month("2021-08-01"))
print(get_first_day_of_month("2020-02-25"))
print(calculate_date("2021-08-25", 10, False))
print(calculate_date("2021-08-25", 10, True))
print(calculate_date("2021-08-25", -10, False))
print(calculate_date("2021-08-25", -10, True))
