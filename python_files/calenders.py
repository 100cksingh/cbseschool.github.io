# part 1
# import calendar

# c=calendar.TextCalendar(calendar.TUESDAY)
# # # st=c.formatday(2017,1,0)
# # st=c.formatmonth(2022,2,1,2)
# # print(st)

# # crete HTML formatted calender
# hc=calendar.HTMLCalendar(calendar.SATURDAY)
# st=hc.formatmonth(2022,2)
# print(st)


# part 2
# import calendar

# c=calendar.TextCalendar(calendar.TUESDAY)

# # crete HTML formatted calender
# # hc=calendar.HTMLCalendar(calendar.SATURDAY)
# # st=hc.formatmonth(2022,2)
# # print(st)

# for i in c.itermonthdays(2022,8):
#     print(i)


# part 3 
# print name of all days and months

# import calendar

# c=calendar.TextCalendar(calendar.SUNDAY)
# # for i in c.itermonthdays(2022,8):
# #     print(i)
    

# for name in calendar.month_name:
#     print(name)

# for day in calendar.day_name:
#     print(day)

# part 4
# find out special days in all months
import calendar

c=calendar.TextCalendar(calendar.SUNDAY)

print("Team meetings will be on:")
for m in range(1,13):
    cal=calendar.monthcalendar(2022,m)
    weekone=cal[0]
    weektwo=cal[1]

    if weekone[calendar.FRIDAY]!=0:
          meetday=weekone[calendar.FRIDAY]
    else:
        meetday=weektwo[calendar.FRIDAY]
    
    print("%10s %2d"%(calendar.month_name[m],meetday))

