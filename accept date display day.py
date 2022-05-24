# this will print  day of the given date
from datetime import*                                             
d,m,y=[int(x) for x in input("Enter a date:").split('/')]
dt=date(y,m,d)
print(dt.strftime("Day %w of the week this is %A"))