def add_time(start, duration, day = ""):
     
  day = day.capitalize()
    
  start_list = start.split(":")
  [start_hour, start_minute] = start_list[0], start_list[1].split()[0]
    
  am_pm = start_list[1].split()[1]
    
  [duration_hour, duration_minute] = duration.split(":")

  hour = int(start_hour) + int(duration_hour)
  minute = int(start_minute) + int(duration_minute)
    
  if minute >= 60:
    hour += (minute // 60)
    minute = minute % 60
    
  days = (hour - int(start_hour)) // 24
  hour_check = (hour - int(start_hour)) % 12

  if am_pm == "PM":
    if (int(start_hour) + hour_check) >= 12:
       days += 1
       am_pm = "AM"
    else:
      if hour_check % 2 != 0:
        am_pm = "AM"
  elif am_pm == "AM":
    if (int(start_hour) + hour_check) >= 12:
      am_pm = "PM"
    elif hour_check % 2 != 0:
      am_pm = "PM"
    
  hour = hour % 12
  if hour == 0:
    hour = 12

  minute = str(minute).zfill(2)
    
  weekdays = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
    
  new_day_value = 0
  new_day = ""

  for key, value in weekdays.items():
    if key == day:
      new_day_value = value + (days % 7)
      while new_day_value > 7:
        new_day_value -= 7
  for key, value in weekdays.items():    
    if new_day_value == value:
        new_day = key 
        print(new_day)
    
  if day != "":
    if days < 1:
      new_time = f"{hour}:{minute} {am_pm}, {new_day}"
    elif days == 1:
      new_time = f"{hour}:{minute} {am_pm}, {new_day} (next day)"
    elif days > 1:
      new_time = f"{hour}:{minute} {am_pm}, {new_day} ({days} days later)"
  elif day == "":
    if days < 1:
      new_time = f"{hour}:{minute} {am_pm}"
    elif days == 1:
      new_time = f"{hour}:{minute} {am_pm} (next day)"
    elif days > 1:
      new_time = f"{hour}:{minute} {am_pm} ({days} days later)"
        
  return new_time

print(add_time("8:16 PM", "466:02", "Tuesday"))