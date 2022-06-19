def add_time(start, duration, day_of_week = False):
  #Reference Lists/Dicts
  days_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
  days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  am_pm_flip = {"AM": "PM", "PM": "AM" } 

  #Getting Info from duration
  duration_tuple = duration.partition(":")
  duration_hours = int(duration_tuple[0])
  duration_minutes = int(duration_tuple[2])

  #Getting Info from start
  start_tuple = start.partition(":")    #(hr, :, min AM/PM)
  start_minutes_tuple = start_tuple[2].partition(" ")    #(min, ,AM/PM )
  start_hours = int(start_tuple[0])
  start_minutes = int(start_minutes_tuple[0])
  am_or_pm = start_minutes_tuple[2]

  days_passed = duration_hours//24

  #end hr/minute value 
  end_minutes = start_minutes + duration_minutes 
  if end_minutes >= 60:
    start_hours += 1
    end_minutes = end_minutes % 60 #Remainder of div by 60
  end_hours = (start_hours+duration_hours) % 12
  amount_am_pm_flips = (start_hours+duration_hours)//12

  end_minutes = end_minutes if end_minutes > 9 else  "0" + str(end_minutes) #e.g. xx:03
  end_hours = 12 if end_hours == 0 else end_hours #%12 can be 0 which is actually 12
  #If start at PM then go over
  if (am_or_pm == "PM" and start_hours + (duration_hours%12) >= 12):
    days_passed += 1
    
  #AM/PM Check
  am_or_pm = am_pm_flip[am_or_pm] if amount_am_pm_flips%2 == 1 else am_or_pm

  endTime = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm
  #Opt. Arg
  if day_of_week:
    day_of_week = day_of_week.lower()
    new_index = int(days_index[day_of_week]+days_passed)%7
    endDay = days_list[new_index]
    endTime += ", " + endDay

  if days_passed == 1:
    endTime += " " + "(next day)"
  elif days_passed > 1:
    endTime += " (" + str(days_passed) + " days later)"

  return endTime
