class Solution:
    def numSquares(self, n: int) -> int:

        squares = []

        i = 1

        while i * i <= n:
            squares.append(i * i)
            i += 1

        if n == squares[-1]:
            return 1

        s_l = len(squares)

        left = 0
        right = s_l - 1

        while left <= right:
            sum_ = squares[left] + squares[right]

            if sum_ == n:
                return 2
            elif sum_ < n:
                left += 1
            elif sum_ > n:
                right -= 1

        for square in squares:
            to_find = n - square
            left = 0
            right = s_l - 1

            while left <= right:
                sum_ = squares[left] + squares[right]

                if sum_ == to_find:
                    return 3
                elif sum_ < to_find:
                    left += 1
                elif sum_ > to_find:
                    right -= 1

        return 4