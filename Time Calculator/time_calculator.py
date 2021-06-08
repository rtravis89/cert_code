def add_time(start, duration, starting_day = None):
    """Adds the duration time to the start time and prints a formatted string of resulting time"""
    
    week_num_dict = {
        "sunday":0,
        "monday":1,
        "tuesday":2,
        "wednesday":3,
        "thursday":4,
        "friday":5,
        "saturday":6
        }
    
    
    ## Split time
    tm,period = start.split(' ')
    
    st_hr,st_min = map(int,tm.split(":"))
    dr_hr,dr_min = map(int,duration.split(":"))
    
    # Add 12 hours if hour is PM
    if period == "PM":
        st_hr += 12
    
    start_numeric = st_hr * 60 + st_min
    duration_numeric = dr_hr * 60 + dr_min
    

    # Determine if duration crosses into subsequent days
    days = (start_numeric + duration_numeric) // (24*60)
    # Get remaining hours and mins, determine day of week
    hours = ((start_numeric + duration_numeric) % (24*60)) // 60
    mins = ((start_numeric + duration_numeric) % (24*60)) % 60
    
    #Determine correct AM/PM 
    if hours >= 12:
        new_period = "PM"
    else:
        new_period = "AM"    

    if hours == 0:
        hours =+ 12
    if hours > 12:
        hours = hours - 12   

    # Get name of day if starting day is not empty
    if starting_day is not None:
        day_num = week_num_dict[starting_day.lower()]
        day_of_week = (day_num + days) % 7
    
        for name,num in week_num_dict.items():
            if num == day_of_week:
                day_of_week_name =  ', ' + name.capitalize()   
    else:
        day_of_week_name = ''     

    time_str = "{}:{:02d}".format(hours, mins) + ' ' + new_period + day_of_week_name     

    # Put it together 
    if days == 0:
        new_time = time_str
    elif days == 1:
        new_time = time_str + " (next day)"
    else:
        new_time = time_str + " (" + str(days) + " days later)"
    
    return new_time