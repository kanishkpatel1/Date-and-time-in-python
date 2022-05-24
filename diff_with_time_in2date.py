#find difference of two dates with time min sec and weeks
from datetime import*
d1=datetime(2004,6,25,8,00,25)#(year,mon,date,hour,min,second)
d2=datetime(2015,5,20,7,55,15)

diff=d2-d1
print(diff)

weeks,days=divmod(diff.days,7)
print("Difference in weeks is",weeks)

hrs,secs=divmod(diff.seconds,3600)
print("Difference in hours is",hrs)

min=secs//6
print("Difference in minute is ",min)

secs=secs%60
print("Difference in sec is",secs)
