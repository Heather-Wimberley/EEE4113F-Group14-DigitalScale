import serial
from datetime import datetime 

# datetime object containing current date and time
now = datetime.now()
arr = [0]*30 
arr2 = [0]*10 
total = 0 
weight = 0

if __name__ == '__main__':
	ser = serial.Serial('/dev/serial0',115200,timeout=1)
	ser.reset_input_buffer()
	while True:
            for i in range(30):
                if ser.in_waiting > 0:
                   line = ser.readline().decode('utf-8').rstrip()
                   arr[i] = int(line) 

	    
            for i in range(0, len(arr)):    
                for j in range(i+1, len(arr)):    
                 if(arr[i] > arr[j]):    
                  temp = arr[i];    
                  arr[i] = arr[j];    
                  arr[j] = temp;


            for x in range(10): 
                arr2[x] = arr[9 + x]

            for i in range(10): 
                total = total + arr2[i]

            weight = total/10 
            break

	# dd/mm/YY H:M:S
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S") 
	with open('results.txt', 'a') as f:
            f.write('\n|ID       |'+str(weight+'        |'+dt_string+'         |'+'\n------------------------------------------------------')

