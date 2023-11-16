import math
from pprint import pprint

import requests

# r = requests.get('https://gbfs.citibikenyc.com/gbfs/fr/station_information.json')
# data = r.json()
#
# for i in data['data']['stations']:
#     print(f"{i['name']}: {i['capacity']}")

# r = requests.get('https://gbfs.citibikenyc.com/gbfs/fr/station_status.json')
# data = r.json()
#
# bike_count = 0
# ebike_count = 0
# for i in data['data']['stations']:
#     bike_count += i['num_bikes_available']
#     ebike_count += i['num_ebikes_available']
#
# print(f"Total bikes: {bike_count}")
# print(f"Total ebikes: {ebike_count}")
# print(f"Ratio ebike: {ebike_count/(bike_count + ebike_count)*100}")


r = requests.get('https://gbfs.citibikenyc.com/gbfs/fr/station_information.json')
data = r.json()

stations = data['data']['stations']
distance_max = 0
st1 = ""
st2 = ""
for station1 in stations:
    for station2 in stations:
        a = station1['lat'] - station2['lat']
        b = station1['lon'] - station2['lon']
        distance = math.sqrt(a * a + b * b)
        if distance > distance_max:
            distance_max = distance
            st1 = station1['name']
            st2 = station2['name']
print(st1)
print(st2)