import datetime as dt

dateNow = dt.datetime.now()
print(dateNow)

# Print current year and month
print("%s %s" % (dateNow.year, dateNow.month))

# Print the current day name
print(dateNow.strftime("%A"))

# Create a date object and print it
customDate = dt.datetime(2005, 4, 8)
print("John Paul II died on: %s" % customDate.strftime("%d %B %Y"))