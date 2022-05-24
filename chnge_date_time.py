# this will replace data from 1 to 2 
from datetime import*
dt1=datetime(year=2020,month=10,day=16,hour=10,minute=30,second=15)
print(dt1)
dt2=dt1.replace(year=2004,month=1,day=7,hour=10,minute=30,second=15)
print(dt2)