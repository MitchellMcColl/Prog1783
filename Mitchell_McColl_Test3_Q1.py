import datetime

t = datetime.datetime.now()
time = t.strftime("%m-%d-%Y, %Hh:%Mm:%Ss")

print("The current date and time is: " + time)