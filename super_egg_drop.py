# def print_matrix(matrix):
#     for row in matrix:
#         for element in row:
#             print(str(element).rjust(2), end=' ')
#         print()
#
#
# def print_coordinates(matrix):
#     for row in matrix:
#         for element in row:
#             print('-'.join([str(element[0]), str(element[1])]).rjust(5), end=' ')
#         print()
#
#  ----- SOLUTION USING DP , where DP[i][j] is a number of  moves needed to solve problem for i eggs and j floors ------
# def superEggDrop(K: int, N: int) -> int:
#     dp = [[0] * (N + 1) for _ in range(K + 1)]
#     MIN_COORDINATES = [[(0, 0)] * (N + 1) for _ in range(K + 1)]
#
#     for i in range(N + 1):
#         dp[1][i] = i
#
#     for i in range(1, K + 1):
#         dp[i][1] = 1
#         dp[i][2] = 2
#
#     for i in range(2, K + 1):
#         for j in range(3, N + 1):
#             possible_min = 1000000000000000
#             for floor in range(1, j):
#                 if_break = dp[i - 1][floor - 1] + 1
#                 if_not_break = dp[i][j - floor] + 1
#
#                 if max(if_break, if_not_break) < possible_min:
#                     if if_break > if_not_break:
#                         MIN_COORDINATES[i][j] = (i - 1, floor - 1)
#                     if if_not_break >= if_break:
#                         MIN_COORDINATES[i][j] = (i, j - floor)
#                 possible_min = min(max(if_break, if_not_break), possible_min)
#
#             dp[i][j] = possible_min
#
#     print_matrix(dp)
#     print("------------")
#     print_coordinates(MIN_COORDINATES)
#     # print(dp[K][N])
#     return dp[K][N]
#
#


# ----- Same solution as above, using binary search to find minimum in LOG time, instead of minimum
# ----- time complexity is K*N*LOG_N (python solution not pass :( , although approach is described in LeetCode)
#
# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         if N <= 2:
#             return N
#
#         dp = [[0] * (N + 1) for _ in range(K + 1)]
#
#         for i in range(N + 1):
#             dp[1][i] = i
#
#         for i in range(1, K + 1):
#             dp[i][1] = 1
#             dp[i][2] = 2
#
#         for i in range(2, K + 1):
#             for j in range(3, N + 1):
#                 possible_min = 10000
#
#                 lo, hi = 1, j - 1
#                 while lo + 1 < hi:
#                     floor = (lo + hi) // 2
#                     if_break = dp[i - 1][floor - 1]
#                     if_not_break = dp[i][j - floor]
#
#                     if if_break < if_not_break:
#                         lo = floor
#                     elif:
#                         hi = floor
#                     else:
#                         lo = hi = floor
#
#                 dp[i][j] = 1 + min(max(dp[i - 1][floor - 1], dp[i][j - floor]) for floor in range(low, hi + 1))
#
#         return dp[K][N]


# Solution pass! now DP[i][j] keeps the maximum floor for which we can solve problem with i eggs, and j moves

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if N <= 2:
            return N

        dp = [[0] * (N + 1) for _ in range(K + 1)]

        for i in range(N + 1):
            dp[1][i] = i

        for i in range(1, K + 1):
            dp[i][1] = 1

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                dp[i][j] = 1 + dp[i][j - 1] + dp[i - 1][j - 1]

        for i in range(2, N + 1):
            if dp[K][i] >= N:
                return i
