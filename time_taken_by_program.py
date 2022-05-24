# to measure the time taken by a program 

from time import*
t1=perf_counter()  #note the starting time of the program
i,sum=0,0

#some processing
while(i<1000):
    sum+=1
    i+=1

sleep(3) #make the processor or evm sleep for 3 seconds

t2=perf_counter()  #to note the ending time
print("Execution time is ",t2-t1)