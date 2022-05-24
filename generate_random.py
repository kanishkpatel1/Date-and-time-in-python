#generate 10 random numbers 
import time,random
for i in range(10):
    num=random.randrange(100,200)
    print(num)
    time.sleep(3.5)  #to suspend execution for 3.5 seconds(stop execution for 3.5 sec in every iteration)