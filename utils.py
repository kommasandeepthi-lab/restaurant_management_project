from datetime import datetime, time

def is_restaurant_open():

    working_hours = {
        0: (time(5, 0), time(22, 0)),
        1: (time(5, 0), time(22, 0)),
        2: (time(5, 0), time(22, 0)),
        3: (time(5, 0), time(22, 0)),
        4: (time(5, 0), time(22, 0)),
        5: (time(8, 0), time(23, 0)),
        6: (time(8, 0), time(20, 0)),
    }

    now = datetime.now()
    current_day = now.weekday()
    current_time = now.time()

    if current_day in working_hours:
        open_time, close_time = working_hours[current_day]

        if open_time < = current_time <= close_time:
            return True

    return False