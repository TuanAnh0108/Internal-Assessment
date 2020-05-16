import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())
info = []
info_1 = []
info_2 = []
name_data = []  # Store the name data of the place
lon_data_string = []  # Store the data of the longtitude (string type)
lat_data_string = []  # Store the data of the latitude (string type)
lon_data = []  # Store the data of the longtitude 
lat_data = []  # Store the data of the latitude
X = []
Y = []
D = []  # Store the distance data for each place

lon_0 = float(lon.replace(",", "."))  # Convert string type to float type
lat_0 = float(lat.replace(",", "."))

for i in range(n):  # Append all the input data into a list
    defib = input()
    info.append(defib)

for i in range(len(info)):  # Split elements in the list by ";"
    word1 = info[i].split(";")
    info_1.append(word1)

for i in range(len(info_1)):
    lon_data_string.append(info_1[i][4])  # Append the longtitude (string type) data
    lat_data_string.append(info_1[i][5])  # Append the latitude (string type) data
    name_data.append(info_1[i][1])  # Append name data of each place

for i in range(len(lon_data_string)):  # Convert string data to float data
    lon_1 = float(lon_data_string[i].replace(",", "."))
    lon_data.append(lon_1)
    lat_1 = float(lat_data_string[i].replace(",", "."))
    lat_data.append(lat_1)

# Calculate the distance
for i in lon_data:
    x = (i - lon_0) * math.cos((i + lon_0) / 2)
    X.append(x)

for i in lat_data:
    y = i - lat_0
    Y.append(y)

for i, j in zip(X, Y):
    d = math.sqrt(i * i + j * j) * 6371
    D.append(d)

# Find the index of the nearest place
index = D.index(min(D))

# Print out the result
print(name_data[index])
