from k_nearest_neighbor import knn
from kdtree import kdtree
from nn_search import nn_search
from utils import get_stations
from knn_with_threading import knn_with_threading

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

        # print('knn ', knn(all_stations, sugg_station))
        # print('nn_search ', nn_search(tree, sugg_station))
        # print('knn_with_threading ', knn_with_threading(all_stations, sugg_station))
        nearest_station_name, distance = knn_with_threading(all_stations, sugg_station)
        print(sugg_station_name, nearest_station_name)


if __name__ == '__main__':
    main()
