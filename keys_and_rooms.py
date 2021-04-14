# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]

        while stack:
            current_room = stack.pop()
            current_keys = rooms[current_room]

            if current_room not in visited:
                visited.add(current_room)

            for key in current_keys:
                if key not in visited:
                    stack.append(key)

        return len(visited) == len(rooms)