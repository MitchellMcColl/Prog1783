import datetime

t = datetime.datetime.now()

print("The current date and time is: " + t.strftime("%B-") + t.strftime("%d-") + t.strftime("%Y  ") + 
t.strftime("%Hh-") + t.strftime("%Mm-") + t.strftime("%Ss"))