def add_time(start_time, duration, starting_day=None):
    # Parse the start time
    start_time_hour, start_time_minute = map(int, start_time[:-3].split(':'))
    start_time_period = start_time[-2:]

    # Parse the duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate the total minutes
    total_minutes = start_time_hour * 60 + start_time_minute + duration_hour * 60 + duration_minute

    # Calculate the new time
    new_time_hour = total_minutes // 60 % 12
    new_time_minute = total_minutes % 60
    new_time_period = start_time_period

    # Determine if it's the next day or later
    days_later = total_minutes // 60 // 12

    # Determine the new period (AM/PM)
    if total_minutes // 60 % 24 >= 12:
        if start_time_period == 'AM':
            new_time_period = 'PM'
        else:
            new_time_period = 'AM'
            days_later += 1

    # Determine the new day of the week
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if starting_day:
        starting_day = starting_day.lower().capitalize()
        starting_day_index = days_of_week.index(starting_day)
        new_day_index = (starting_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]

    # Format the new time string
    new_time = f"{new_time_hour or 12}:{new_time_minute:02d} {new_time_period}"

    # Add the day of the week if provided
    if starting_day:
        new_time += f", {new_day}"

    # Add the number of days later if applicable
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
