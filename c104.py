import csv
with open('HeightWeight.csv',newline='' )as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
#remove the title from the data list
file_data.pop(0)

#sorting data to get the height of the people
new_data = []
for i in range(len(file_data)):
    n_num = file_data [i][1]
    new_data.append(float(n_num))


#find the mean
n = len(new_data)
#print(n)
total = 0
for x in new_data :
    total = total + x

mean = total/n
print("mean is :"+ str(mean))
