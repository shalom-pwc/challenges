# Is-Today-is-Tuesday
# --------------------------------------------
from datetime import datetime

today = datetime.today().strftime('%A')
def today_day():
  if(today == "Tuesday"):
    return "Today is Tusday"
  else:
    return "Today is not Tusday"
print(today_day())
