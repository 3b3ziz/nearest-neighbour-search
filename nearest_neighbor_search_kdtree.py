import math
from sklearn.neighbors import KDTree
import numpy as np

def calc_distance(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))

all_stations = []

routes_num = int(input())
for _ in range(routes_num):
    stations_num = int(input())
    for _ in range(stations_num):
        station_input = input().rstrip().split()

        station_name = station_input[0]
        station_x = int(station_input[1])
        station_y = int(station_input[2])

        station = {
            'name': station_name,
            'coordinates': (station_x, station_y)
        }

        all_stations.append(station)


print(all_stations)

only_coordinates = list(map(lambda x: x['coordinates'], all_stations))
numby_coordinates = np.array(only_coordinates)
kdt = KDTree(numby_coordinates, leaf_size=30, metric='euclidean')

sugg_stations_num = int(input())
for _ in range(sugg_stations_num):
    sugg_station_input = input().rstrip().split()

    sugg_station_name = sugg_station_input[0]
    sugg_station_x = int(sugg_station_input[1])
    sugg_station_y = int(sugg_station_input[2])

    sugg_station = {
        'name': sugg_station_name,
        'coordinates': (sugg_station_x, sugg_station_y)
    }

    nearest_station = ''
    minimum_distance = 10 ** 10

    dist, ind = kdt.query(np.array([sugg_station['coordinates']]), k=1)
    # print(dist, ind)
    print(ind[0])