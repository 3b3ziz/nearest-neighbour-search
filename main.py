from k_nearest_neighbor import knn
from kdtree import kdtree
from nn_search import nn_search
from utils import get_stations
from knn_with_multiprocessing import knn_with_multiprocessing

from itertools import combinations
from time import process_time


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
        # print('knn_with_multiprocessing ', knn_with_multiprocessing(all_stations, sugg_station))
        nearest_station_name, distance = knn_with_multiprocessing(all_stations, sugg_station)
        print(sugg_station_name, nearest_station_name)

    # print('Measuring Performance: ')
    # test_stations = list(map(lambda s: ('T', s),
    #                          list(combinations(range(1000), 2))))
    # tree = kdtree(test_stations)
    # test_station = ('R', (22, 22))

    # t = process_time()
    # print('knn ', knn(test_stations, test_station))
    # elapsed_time = process_time() - t
    # print('elapsed_time ', elapsed_time)

    # t = process_time()
    # print('nn_search ', nn_search(tree, test_station))
    # elapsed_time = process_time() - t
    # print('elapsed_time ', elapsed_time)

    # t = process_time()
    # print('knn_with_multiprocessing ', knn_with_multiprocessing(test_stations, test_station, 3))
    # elapsed_time = process_time() - t
    # print('elapsed_time ', elapsed_time)


if __name__ == '__main__':
    main()
