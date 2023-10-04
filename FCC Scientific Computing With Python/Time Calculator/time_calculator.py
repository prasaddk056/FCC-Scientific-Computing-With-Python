def add_time(start, duration, starting_day=""):

  # Seperate the start into hours and minutes
  pieces = start.split()
  time = pieces[0].split(":")
  end = pieces[1]

  # Converting 24 hour clock format
  if (end == "PM"):
    hour = int(time[0]) + 12
    time[0] = str(hour)

  # Separate the duration into hours and minutes
  dur_time = duration.split(":")

  # Add hours and minutes
  new_hour = int(time[0]) + int(dur_time[0])
  new_minutes = int(time[1]) + int(dur_time[1])

  if (new_minutes >= 60):
    hr_add = new_minutes // 60
    new_minutes -= hr_add * 60
    new_hour += hr_add

  days_add = 0

  if (new_hour > 24):
    days_add = new_hour // 24
    new_hour -= days_add * 24

  # Find AM & PM and Converting to 12 hour clock format
  if (new_hour > 0 and new_hour < 12):
    end = "AM"
  elif (new_hour == 12):
    end = "PM"
  elif (new_hour > 12):
    end = "PM"
    new_hour -= 12
  else:
    # new_hour == 0
    end = "AM"
    new_hour += 12

  # Calculating the days_later
  days_later = ""
  if (days_add > 0):
    if (days_add == 1):
      days_later = " (next day)"
    else:
      days_later = f" ({days_add} days later)"


  # Calculating day from starting_day
  week_days = ("monday", "tuesday", "wednesday", "thursday", "friday","saturday", "sunday")

  if starting_day :
    weeks = days_add // 7
    i = week_days.index(starting_day.lower()) + (days_add - 7 * weeks)

    if i > 6 :
      i -= 7
    
    day = f", {week_days[i].capitalize()}"
  
  else:
    day = ""

  # formatting new_minutes
  if(new_minutes <= 9):
    new_minutes = f"0{new_minutes}"

  new_time = f"{new_hour}:{new_minutes} {end}{day}{days_later}"
  
  return new_time
