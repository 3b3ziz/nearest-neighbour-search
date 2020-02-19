# nearest-neighbour-search

This application solves the nearest neighbour search problem with multiple approches.

1. First Approach:
Using KNN algorithm which is an exact algorithm with complexity O(n). The advanatage of this algorithm is that it always returns an exact solution. However, its complexity increases linearly with the number of points (stations).

2. Second Approach:
Using KDtree data structure to speed up the search from O(n) to O(log n). In addition, O(nlog n) to construct the tree itself. However, the main disadvantage of this algorithm is that it is not an exact algorithm.

3. Third Approach:
Using First Approach but with multi-processing through splitting our array of points into m sub-arrays where m is the number of processes. Each process searches through the sublist and eventually an m-length array is constructed. However, for a small number of points, this algorithm would not be very efficient since multi-processing adds complexity due to shared memory communication among processes.
