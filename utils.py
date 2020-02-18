import math


def calc_distance(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))


def get_stations():
    all_stations = []
    routes_num = int(input())
    for _ in range(routes_num):
        stations_num = int(input())
        for _ in range(stations_num):
            station_input = input().rstrip().split()

            station_name = station_input[0]
            station_x = int(station_input[1])
            station_y = int(station_input[2])

            station = (station_name, (station_x, station_y))

            all_stations.append(station)
    return all_stations
