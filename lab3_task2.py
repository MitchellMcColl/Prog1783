days = 0.0
hours = 0.0
mins = 0.0

def daysToMinutes(days):
    return days * 1440
    

def hoursToMinutes(hours):
    return hours * 60
    

def displayMinutes(days, hours, mins):
    print("The value of " + str(days) + " days and " + str(hours) + " hours in minutes is: " + str(mins))
    


days = float(input("Please enter the number of days you want to conver to minutes: "))
hours = float(input("Please enter the amount of hours you want to convert to minutes: "))

mins = daysToMinutes(days)
mins += hoursToMinutes(hours)
displayMinutes(days, hours, mins)