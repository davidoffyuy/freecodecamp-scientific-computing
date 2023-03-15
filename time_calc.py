day_to_num = {"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
num_to_day = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}

# REFERENCE
# Hour: 60min
# Day: 1440min
# Week: 10080min

def add_time(start, duration, day = None):
    # BEGIN: breakdown start inputs
    tempStr = start.split(" ")
    start_ampm = tempStr[1]
    tempStr = tempStr[0].split(":")
    if start_ampm == "PM":
        start_hour = int(tempStr[0]) + 12
    else:
        start_hour = int(tempStr[0])
    start_min = int(tempStr[1])
    # END
    
    # BEGIN: calculate start absolute minutes
    start_abs_min = int(start_min) + 60 * int(start_hour)
    if not day is None:
        start_abs_min = start_abs_min + 1440 * (day_to_num[day.lower()] - 1)
    # END

    # BEGIN: breakdown duration inputs and calculate duration absolute minutes
    tempStr = duration.split(":")
    duration_hour = int(tempStr[0])
    duration_min = int(tempStr[1])
    duration_abs_min = duration_hour * 60 + duration_min
    # END

    print("Start:", start, " Duration:", duration, " Day:", day)
    print("Start Absolute Minute:", start_abs_min) #mark
    print("Duration Absolute Minute:", duration_abs_min) #mark

    # Add the duration to the start time.
    # Reverse logic to determin what day/time it is.

    new_time = calc_date_time(start_abs_min, duration_abs_min, day)
    print("New Time:", new_time)
    return new_time

# Functions 
def calc_date_time(start, duration, day = None):
    final_abs_time = start + duration
    (start_days, start_min_remain) = divmod(start, 1440)
    (final_days, final_min_remain) = divmod(final_abs_time, 1440)
    days_change = final_days - start_days

    if final_min_remain < 720:
        final_ampm = "AM"
    else:
        final_ampm = "PM"
        final_min_remain -= 720

    (final_hours, final_min) = divmod(final_min_remain, 60)
    if final_hours == 0:
        final_hours = 12

    final_string = str(final_hours) + ":" + str(final_min).zfill(2) + " " + final_ampm

    # BEGIN Determine which day the new day starts at
    if not day is None:
        final_day = (day_to_num[day.lower()] + days_change) % 7
        if final_day == 0:
            final_day = 7
        print("Final Day:", final_day)
        final_day_of_week = num_to_day[final_day]
        final_string += ", " + final_day_of_week
    # END

    # BEGIN Append the number of days later to return string ie. (next day), (10 days later)
    if days_change == 1:
        final_string += " (next day)"
    elif days_change > 1:
        final_string += " (" + str(days_change) + " days later)"
    # END

    return final_string