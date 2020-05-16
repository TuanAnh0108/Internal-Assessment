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
name_data = []
lon_data_string = []
lat_data_string = []
lon_data = []
lat_data = []
X = []
Y = []
D = []

lon_0 = float(lon.replace(",", "."))
lat_0 = float(lat.replace(",", "."))

for i in range(n):
    defib = input()
    info.append(defib)

for i in range(len(info)):
    word1 = info[i].split(";")
    info_1.append(word1)

for i in range(len(info_1)):
    lon_data_string.append(info_1[i][4])
    lat_data_string.append(info_1[i][5])
    name_data.append(info_1[i][1])


for i in range(len(lon_data_string)):
    lon_1 = float(lon_data_string[i].replace(",", "."))
    lon_data.append(lon_1)
    lat_1 = float(lat_data_string[i].replace(",", "."))
    lat_data.append(lat_1)

for i in lon_data:
    x = (i - lon_0) * math.cos((i + lon_0) / 2)
    X.append(x)

for i in lat_data:
    y = i - lat_0
    Y.append(y)

for i, j in zip(X, Y):
    d = math.sqrt(i * i + j * j) * 6371
    D.append(d)

index = D.index(min(D))

print(name_data[index])