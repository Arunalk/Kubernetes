with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

import csv

'''
Traditional method
'''
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        if row[2] != "temperature":
            temp.append(int(row[2]))
    print(temp)

'''
Pandas
'''

import pandas

data = pandas.read_csv("weather_data.csv")
print(data['temperature'])

'''
Type checks
'''

print(type(data))
'''
Conversion type of whole table
'''
data_dict = data.to_dict()
print(data_dict)

'''
Convert type for a column
'''
temp_list = data["temperature"].to_list()
print(temp_list)

'''
Average of temperatures using traditional method
'''
avg = sum(temp_list)/len(temp_list)
print(avg)

'''
Using pandas to find average
'''
print(data["temperature"].median())
#max
print(data["temperature"].max())

# Get data in column

print(data['location'])
print(data.location)

# Get Data in Row
print(data[data.date == '2025-05-10'])

# Data of row which has max temp
print(data[data.temperature == data.temperature.max()])

#Monday location
monday = data[data.date == '2025-05-10']
print(monday.temperature)

#Converting from C to F

monday_temperature_F = monday.temperature[0] * 9/5
print(monday_temperature_F)

'''
Creating a datafrom from Scratch
'''
data_dict = {
    "students": ["stu-1", "stu-2", "stu-3"],
    "scores": [96, 70, 50]
}

data = pandas.DataFrame(data_dict)
print(data)
# convert to csv
data.to_csv("data.csv")