from utils import calc_distance

def knn(all_stations, sugg_station, nearest_stations = []):
    nearest_station = ''
    minimum_distance = 10 ** 10
    for station in all_stations:
        diff = calc_distance(station[1], sugg_station[1])
        if diff < minimum_distance:
            minimum_distance = diff
            nearest_station = station[0]

    nearest_stations.append((nearest_station, minimum_distance))
    return (nearest_station, minimum_distance)
