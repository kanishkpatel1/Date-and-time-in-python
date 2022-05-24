# this program will tell the todays day ex...>sunday and the no in 365 days
from datetime import*
td=date.today()
print(td)
s1=td.strftime("%j")
print("Today is ",s1,'th day of the current year')

s2=td.strftime("%A")
print("It is ",s2)