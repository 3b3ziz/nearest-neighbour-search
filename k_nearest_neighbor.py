from utils import calc_distance


def knn(all_stations, sugg_station, nearest_stations=[],
        nearest_stations_distances=None, nearest_stations_names=None, index=0):
    nearest_station = ''
    minimum_distance = float('inf')
    for station in all_stations:
        diff = calc_distance(station[1], sugg_station[1])
        if diff < minimum_distance:
            minimum_distance = diff
            nearest_station = station[0]

    nearest_stations.append((nearest_station, minimum_distance))
    if nearest_stations_distances:
        nearest_stations_distances[index] = minimum_distance
    if nearest_stations_names:
        nearest_stations_names[index] = nearest_station
    return (nearest_station, minimum_distance)
