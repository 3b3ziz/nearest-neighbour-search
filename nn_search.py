from utils import calc_distance


def nn_search(tree, point, depth: int = 0):

    current_best = 10 ** 10
    nearest_station = None

    def nn_search_helper(point, tree, depth: int = 0):
        nonlocal current_best
        nonlocal nearest_station

        if not tree:
            return None

        k = len(tree.location)
        axis = depth % k

        # compare distance between my search point and the node location
        # store current_best values
        distance = calc_distance(point[1], tree.location[1])

        if distance < current_best:
            current_best = distance
            nearest_station = tree.location

        if point[1][axis] < tree.location[1][axis]:
            nn_search_helper(point, tree.left_child, depth + 1)
        else:
            nn_search_helper(point, tree.right_child, depth + 1)

    nn_search_helper(point, tree, depth)

    return nearest_station[0], current_best, 
