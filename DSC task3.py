#print the date bases on the day number and year
import datetime
def date():
    daynum=int(input("enter day number"))
    year=int(input("enter year"))
    jan1=datetime.date(year,1,1)
    d=jan1+datetime.timedelta(daynum-1)
    print(d.strftime("%d %b, %Y"))
date()
