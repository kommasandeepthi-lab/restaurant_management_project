import datetime

def is_restaurant_open():

    now = datetime.datetime.now()
    current_day = now.weekday()
    current_time = now.time()

    weekday_open = datetime.time(9, 0)
    weekday_close = datetime.time(22, 0)
    weekday_open = datetime.time(10, 0)
    weekday_close = datetime.time(23, 0)

    if current_day < 5:
        return weekday_open <= current_time <= weekday_close
    else:
        return weekday_open <= current_time <= weekend_close