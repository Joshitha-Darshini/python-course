from datetime import date,time,datetime
#calling the today
#function of the date class
today=date.today()
now = datetime.now()
print("todays's date is", now)
print("\ncurent date and time is ", now)
#printing date's components
print("\ndate components", today.year,today.month ,today.day)