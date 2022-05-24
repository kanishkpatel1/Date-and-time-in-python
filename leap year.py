#to check the year is leap or not by using modules
from calendar import*

y=int(input("Enter the year:"))
if(isleap(y)):
    print("Leap Year")
else:
    print("Year is not the leap year")
