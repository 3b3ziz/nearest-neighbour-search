from utils import calc_distance


def nn_search(point, tree, depth: int = 0, current_best=10 ** 10, best_values=[]):
    if not tree:
        return None

    k = len(tree.location)
    axis = depth % k

    # compare distance between my search point and the node location
    # store current_best values
    distance = calc_distance(point[1], tree.location[1])
    print(point[1], tree.location[1])
    if distance < current_best:
        current_best = distance
        best_values.append((tree.location[0], current_best))

    if point[1][axis] < tree.location[1][axis]:
        nn_search(point, tree.left_child, depth + 1, current_best, best_values)
    else:
        nn_search(point, tree.right_child, depth +
                  1, current_best, best_values)

    return best_values
