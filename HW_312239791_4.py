import requests
import json
dist = dict()
key = "please enter you key"
#please enter the path and the file name
file = open("C:/Users/keren/Desktop/PY/dests (1).txt")
data = []
#connect to the internet page and save in the informetion of the distance
for line in file:
    data.append(line.strip())
#the url with all the cities
url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=jerusalem&destinations=" + "|".join(data)+ "&key=" + key
try:
    response = requests.get(url)
    if not response.status_code == 200:
        print("HTTP error")
    else:
        response = requests.get(url)
        response_json = response.json()
except:
    print("Something went wrong with requests.get")
#connect to the internet page and save in the informetion of the lat and lng
url_location = "https://maps.googleapis.com/maps/api/geocode/json?address=" + "|".join(data) + "&key=" + key
response = requests.get(url_location)
if not response.status_code == 200:
    print("HTTP error")
else:
     response = requests.get(url_location)
     loc_json = response.json()
#print the distance and duration
for i in range(len(data)):
    x =  "\n distance from Jerusalem: " + response_json['rows'][0]['elements'][i]['distance']['text'] + "; duration: "
    time = str(round(response_json['rows'][0]['elements'][i]['duration']['value']/60))
    print(data[i] + x + time)

#print the lat and lng
for i in range(len(data)):
    x = data[i] + "\n" + str(loc_json['results'][i]['geometry']['location'])
    print(x)

#save all the data in dict (we celled it 'dist') and print it
for i in range(len(data)):
    x = response_json['rows'][0]['elements'][i]['distance']['text']
    time = str(response_json['rows'][0]['elements'][i]['duration']['text'])
    lat = loc_json['results'][i]['geometry']['location']['lat']
    lng = loc_json['results'][i]['geometry']['location']['lng']
    info_ = (x, time,lat,lng)
    dist[data[i]] = info_
for i in dist:
    print(i, "\n distance from Jerusalem: ", dist[i][0], "\n The duration: ",dist[i][1],"\n lat:", dist[i][2], "\n lng:", dist[i][3])
#The 3 furthest cities from Jerusalem

far = []
for i in dist:
    far.append(int(dist[i][0].split()[0].replace(",", "")))
far.sort(reverse = True)
print ("The 3 furthest cities from Jerusalem are:")
for i in range(3):
    for k,v in dist.items():
        z = v[0].split()[0].replace(",", "")
        z = int(z)
        if z==far[i]:
            print(k, far[i], "km from Jerusalem")