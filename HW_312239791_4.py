import requests
import json

dist = dict()
key = "AIzaSyByS69KCJmj0sn_x9Ejse1SE3s98H5LL5Y"
file = open("C:/Users/keren/Desktop/PY/dests (1).txt")
data = []
for line in file:
    data.append(line.strip())

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=jerusalem&destinations=" + "|".join(
    data) + "&key=" + key
try:
    response = requests.get(url)
    if not response.status_code == 200:
        print("HTTP error")
    else:
        response = requests.get(url)
        response_json = response.json()
        print(url)
except:
    print("Url not found")

for i in range(len(data)):
    x =  "\n distance from Jerusalem: " + response_json['rows'][0]['elements'][i]['distance']['text'] + "; duration: "
    time = str(round(response_json['rows'][0]['elements'][i]['duration']['value']/60))
    print(data[i] + x + time)

url_location = "https://maps.googleapis.com/maps/api/geocode/json?address=" + "|".join(data) + "&key=" + key
response = requests.get(url_location)
if not response.status_code == 200:
    print("HTTP error")
else:
     response = requests.get(url_location)
     loc_json = response.json()
for i in range(len(data)):
    x = data[i] + "\n" + str(loc_json['results'][i]['geometry']['location'])
    print(x)

for i in range(len(data)):
    x = response_json['rows'][0]['elements'][i]['distance']['text']
    time = str(response_json['rows'][0]['elements'][i]['duration']['text'])
    lat = loc_json['results'][i]['geometry']['location']['lat']
    lng = loc_json['results'][i]['geometry']['location']['lng']
    info_ = (x, time, lat, lng)
    dist[data[i]] = info_

print(dist)