from datetime import datetime
import time, json

with open("./config.json", "r") as r:
  config = json.load(r)

def update():
  global year, month, day, hour, minute, second, unit
  current = datetime.now().astimezone()
  if config["system"]["timezone"] != time.tzname[0]:
    config["system"]["timezone"] = time.tzname[0]
    with open("./config.json", "w") as w:
      json.dump(config, w, indent=4)

  year = current.year
  month = current.month
  day = current.day
  hour = current.hour
  minute = current.minute
  second = current.second
  unit = None

  if config["system"]["timeFormat"] == 12:
    rawHour = hour
    hour = rawHour % 12 or 12
    unit = "AM" if rawHour < 12 else "PM"
  elif config["system"]["timeFormat"] == 24:
    pass
