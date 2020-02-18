from threading import Thread
from utils import calc_distance
from utils import chunks
from k_nearest_neighbor import knn


def knn_with_threading(all_stations, sugg_station, threads_num=4):
    stations_num = len(all_stations)
    nearest_stations = []
    thread_list = []

    # We take the minimum of threads number and stations number
    # not to try -for example- to split array of 9 stations into 10 threads
    chunks_num = min(threads_num, stations_num)
    stations_chunks = list(chunks(all_stations, chunks_num))

    for chunk in stations_chunks:
        t = Thread(target=knn, args=(chunk, sugg_station, nearest_stations, ))
        thread_list.append(t)
        t.start()

    for thread in thread_list:
        thread.join()

    nearest_station = min(nearest_stations, key=lambda x: x[1])
    return nearest_station
