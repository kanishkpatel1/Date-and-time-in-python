# to know who is older in two persons
from datetime import*                                             
d1,m1,y1=[int(x) for x in input("Enter the dob of first person:").split('/')]
                                       
d2,m2,y2=[int(x) for x in input("Enter the dob of second person:").split('/')]
dt1=date(y1,m1,d1)
dt2=date(y2,m2,d2)
if(dt1==dt2):
    print("Both are equal ages:")
elif(dt1>dt2):
    print("The second person is older:")
else:
    print("the first person is older")