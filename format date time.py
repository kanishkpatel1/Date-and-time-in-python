# two types of printing date today
from datetime import*
td=date.today()
print(td)

str=td.strftime("%d,%B,%Y")
print(str) 