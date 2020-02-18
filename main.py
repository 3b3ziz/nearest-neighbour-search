from k_nearest_neighbor import knn
from kdtree import kdtree
from nn_search import nn_search
from utils import get_stations

def main():
    all_stations = get_stations()
    tree = kdtree(all_stations)

    sugg_stations_num = int(input())
    for _ in range(sugg_stations_num):
        sugg_station_input = input().rstrip().split()

        sugg_station_name = sugg_station_input[0]
        sugg_station_x = int(sugg_station_input[1])
        sugg_station_y = int(sugg_station_input[2])

        sugg_station = (sugg_station_name, (sugg_station_x, sugg_station_y))

        x, y = knn(all_stations, sugg_station)
        print(x, y)
        print(nn_search(sugg_station, tree, 0, 10**10, []))


if __name__ == '__main__':
    main()
