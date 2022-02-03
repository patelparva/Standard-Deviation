import csv
import math

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

total=0
n=len(data)

for i in data:
    total=total+int(i)

mean=total/n

squared_list=[]

for i in data:
    a=int(i)-mean
    b=a**2
    squared_list.append(b)

total_of_squares=0
for i in squared_list:
    total_of_squares+=i

c=total_of_squares/(n-1)

standard_deviation=math.sqrt(c)

print('Standard deviation is '+str(standard_deviation))