import math
def calc_distance(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))

all_stations = []

# routes = []
routes_num = int(input())
for _ in range(routes_num):
    # new_route = []
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
        # new_route.append(station)

        all_stations.append(station)

    # routes.append(new_route)
# print(routes)




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
    # print(sugg_station_name)
    # for r in routes:
        # for station in r:
    for station in all_stations:
        diff = calc_distance(station['coordinates'], sugg_station['coordinates'])
        print(station, diff)
        if diff < minimum_distance:
            minimum_distance = diff
            nearest_station = station['name']
    print(sugg_station_name, nearest_station)
