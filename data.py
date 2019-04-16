import csv
 
user = []
time = []
x = []
y = []
distance = []
velocity = []
acceleration = []
jerk = []
angle = []
anglev = []

attributes = []

with open('touchdata_test.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
	user.append(row[0])
	time.append(row[1])
	x.append(row[2])
	y.append(row[3])
	distance.append(row[4])
	velocity.append(row[5])
	acceleration.append(row[6])
	jerk.append(row[7])
	angle.append(row[8])
a = 1

attributes = [user[a], time[a], x[a], y[a], distance[a], velocity[a], acceleration[a], jerk[a], angle[a]]

print(attributes[1:8])
