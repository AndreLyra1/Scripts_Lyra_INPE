import datetime

def example_function_utils():
    print ("this is a function imported from the utils.py module.")

def date_as_datetime(year,month,day,hour):
    date_in_datetime = datetime.datetime(
            int(year), 
            int(month), 
            int(day), 
            int(hour)
        )
    return date_in_datetime

def date_as_YYYYMMDDHH_str(year,month,day,hour):
    date_in_string = f"{year}{month}{day}{hour}" 
    return date_in_string

def get_final_date_from_initial_date(date_in_datetime, time_window):
    date_final_in_datetime = date_in_datetime + datetime.timedelta(hours=time_window)
    return date_final_in_datetime