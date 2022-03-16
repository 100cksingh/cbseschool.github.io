# part 1 here is problem in codes 
# from datetime import date
# from datetime import time
# from datetime import datetime

# def main():
#     today=date.today()
#     print("Today's date is",today)

#     print("Date components:",today.day,today.month,today.year)

# part 2 
# using timedelata objects 
# no problems in codes 

    
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365,hours=5,minutes=1))

now=datetime.now()
print("today is:"+str(now))

print("one year from now it will be:"+str(now +timedelta(days=365)))
print("In 2 days and 3 weeks,it will be "+str(now +timedelta(days=2,weeks=3)))

t=datetime.now()-timedelta(weeks=1)
s=t.strftime("% A %B %d,%Y")
print("one week ago it was :"+s)

# How many days until April Fool's day ?
today=date.today()
afd=date(today.year,4,1)

if afd<today:
    print("April Fool's day already went by %d days ago"%((today-afd).days))
    afd=afd.replace(year=today.year+1)

# now calculate the amount of time until April Fool's Day
time_to_afd=afd-today
print("It's just",time_to_afd.days,"days until April Fool's Day")

# output is

# 365 days, 5:01:00
# today is:2022-02-27 05:10:15.134155
# one year from now it will be:2023-02-27 05:10:15.134155
# In 2 days and 3 weeks,it will be 2022-03-22 05:10:15.134155
# one week ago it was :% A February 20,2022
# It's just 33 days until April Fool's Day

