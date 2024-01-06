import math
num = int( input ("Enter a number: "))
for i in range (0 , num):
    for j in range (0 , int (math.log(num))):
        i += 1
        j += 1
for k in range (0 , num , 2):
    k += 1 
print (i)
print ("The end.")