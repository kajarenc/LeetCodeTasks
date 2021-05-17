# https://leetcode.com/problems/car-pooling/
from typing import List
from collections import defaultdict

# My solution


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True

        trips_points = []

        for trip in trips:
            trips_points.append(trip[1])
            trips_points.append(trip[2])

        trips_points = list(set(trips_points))
        trips_points.sort()

        trips_start_dict = defaultdict(int)
        trips_end_dict = defaultdict(int)

        for trip in trips:
            trips_start_dict[trip[1]] += trip[0]
            trips_end_dict[trip[2]] += trip[0]

        busy_seats = 0

        for point in trips_points:
            if point in trips_end_dict:
                busy_seats -= trips_end_dict[point]

            if point in trips_start_dict:
                busy_seats += trips_start_dict[point]
                if busy_seats > capacity:
                    return False
        return True

    # Beautiful solution from discussions
    def carPoolingDiscussions(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True
