# this program is to short dates
from datetime import*

group=[]
group.append(date.today()) # append today's date into the group

d=date(2015,10,25)
group.append(d)
d=date(2016,10,25)
group.append(d)

group.append(d+timedelta(days=20))

group.sort()

for d in group:
    print(d)