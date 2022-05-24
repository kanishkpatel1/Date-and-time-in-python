#finding future date and time
from datetime import*
d1=datetime(2022,5,7,16,45,0) #Enter the bigining date
period1=timedelta(days=10,seconds=10,minutes=10,hours=12)
print("The new date and time is :",d1+period1)