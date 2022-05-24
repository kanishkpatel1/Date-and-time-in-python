#combine date and time 
from datetime import*
d=date(2004,10,16)
t=time(15,30)
dt=datetime.combine(d,t)
print(dt)