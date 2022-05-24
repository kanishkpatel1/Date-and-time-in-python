#to print 10 dates continuously
from datetime import*
d=date.today() #this is for today date otherwise we can give andy date -------> date(1992,6,29)
print(d)
 
for i in range(1,10):
    nextdate=d+timedelta(days=i)
    print(nextdate)