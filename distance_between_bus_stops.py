from typing import List

# https://leetcode.com/problems/distance-between-bus-stops/


def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    start, destination = min(start, destination), max(start, destination)
    clockwise = sum(distance[start:destination])
    not_clockwise = sum(distance) - clockwise
    return min(clockwise, not_clockwise)
