import datetime
from datetime import timedelta

class DateUtils:
    @staticmethod
    def get_current_time():
        return datetime.datetime.now().strftime('%H:%M:%S')
    
    @staticmethod
    def is_day_weekends(date_str):
        return datetime.datetime.isoweekday(datetime.date.fromisoformat(date_str)) > 6
        
    @staticmethod
    def calculate_date(date_str, calc_date, skip_weekends):
        date = datetime.date.fromisoformat(date_str) 
        passDays = 0
        if skip_weekends:
            week_ends_count = 0
            work_days_count = 0
            if calc_date < 0:
                while (work_days_count > calc_date) :
                    if datetime.datetime.isoweekday(date + timedelta(days=passDays)) < 6:
                        work_days_count -= 1
                    else : 
                        week_ends_count -= 1
                    passDays += 1
            elif calc_date > 0:
                while (work_days_count < calc_date) :
                    if datetime.datetime.isoweekday(date + timedelta(days=passDays)) < 6:
                        work_days_count += 1
                    else :
                        week_ends_count += 1
                    passDays += 1
    
            calc_date += week_ends_count
        return str(date + timedelta(days=calc_date))
    
    @staticmethod
    def get_last_day_of_month(date_str) :
        date = datetime.date.fromisoformat(date_str)
        return str((date.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1))
    
    @staticmethod
    def get_first_day_of_month(date_str) :
        date = datetime.date.fromisoformat(date_str)
        return str(date.replace(day=1))


