#print current date and time
from datetime import*
now=datetime.now()
print(now)
print("Date now :%d /%d/%d"%(now.day,now.month,now.year))
print("Time now :%d:%d:%d"%(now.hour,now.minute,now.second))
