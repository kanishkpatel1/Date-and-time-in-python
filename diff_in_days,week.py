#difference between two dates with days ,weeks,months
from datetime import*                                             
d1,m1,y1=[int(x) for x in input("Enter the first date:").split('/')]
                                       
d2,m2,y2=[int(x) for x in input("Enter the second date:").split('/')]
dt1=date(y1,m1,d1)
dt2=date(y2,m2,d2)
dt=dt1-dt2
print("Days difference:",dt)

weeks,days=divmod(dt.days,7)
print("Weeks deifference:",weeks)

months,days=divmod(dt.days,30)
print("Months difference=",months)
