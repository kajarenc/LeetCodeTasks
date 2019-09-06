
# https://leetcode.com/problems/coin-change-2/
# video explanation: https://youtu.be/DJ4a7cmjZY0


def change(amount: int, coins: List[int]) -> int:
    DP = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

    for i in range(len(DP)):
        DP[i][0] = 0

    DP[0][0] = 1

    n = len(DP)
    m = len(DP[0])

    for i in range(1, n):
        for j in range(m):
            if i-1 >= 0:
                DP[i][j] += DP[i-1][j]

            new_coin_amount = coins[i - 1]

            if j - new_coin_amount >= 0:
                DP[i][j] += DP[i][j-new_coin_amount]

    return DP[-1][-1]
