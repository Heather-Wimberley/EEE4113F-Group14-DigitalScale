import random
from datetime import datetime


arr1 = [0]*30 
arr2 = [0]*10
total = 0 
weight = 0

for i in range(30): 
	arr1[i] = 220 + random.randint(0,9) 

#for x in range(30): 
#	print(arr1[x])

for i in range(0, len(arr1)):
    for j in range(i+1, len(arr1)):
        if(arr1[i] > arr1[j]):
            temp = arr1[i]
            arr1[i] = arr1[j]
            arr1[j] = temp

#print("Elements of array sorted in ascending order: ")
#for i in range(0, len(arr1)):
#    print(arr1[i], end=" ")

for i in range(10): 
    arr2[i] = arr1[9+i] 

for i in  range(0, len(arr2)): 
    total = total + arr2[i] 

weight = total/10
print(weight, end=" ")

# datetime object containing current date and time
now = datetime.now() 


# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") 


with open('results.txt', 'a') as f:
    f.write('\n|ID      |'+str(weight)+'          |'+dt_string+' |') 
    f.write('\n-----------------------------------------------')
