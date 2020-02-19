from multiprocessing import Process, Array, Manager
from utils import calc_distance
from utils import chunks
from k_nearest_neighbor import knn
from ctypes import Structure, c_double, c_char, c_wchar


def knn_with_multiprocessing(all_stations, sugg_station, processes_num=4):
    stations_num = len(all_stations)
    process_list = []
    # We take the minimum of processes number and stations number
    # not to try -for example- to split array of 9 stations into 10 processes
    chunks_num = min(processes_num, stations_num)
    stations_chunks = list(chunks(all_stations, chunks_num))

    # Shared memory solutions across processes
    # processes_manager = Manager()
    # nearest_stations = processes_manager.list()
    nearest_stations = []
    nearest_stations_distances = Array(c_double, chunks_num)
    nearest_stations_names = Array(c_wchar, chunks_num)

    for index, chunk in enumerate(stations_chunks):
        t = Process(target=knn, args=(chunk, sugg_station,
                                      nearest_stations, nearest_stations_distances,
                                      nearest_stations_names, index))
        process_list.append(t)

    for process in process_list:
        process.start()

    for process in process_list:
        process.join()

    # nearest_station = min(nearest_stations, key=lambda x: x[1])
    nearest_distances = list(nearest_stations_distances)
    min_distance = min(nearest_distances)
    min_index = nearest_distances.index(min_distance)
    return nearest_stations_names[min_index], min_distance
