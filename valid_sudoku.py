from typing import List

# https://leetcode.com/problems/valid-sudoku/


def isValidSudoku(board: List[List[str]]) -> bool:
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    rows_number = len(board)
    columns_number = len(board[0])

    for row in board:
        row_digits = [digit for digit in row if digit in digits]
        if len(row_digits) != len(set(row_digits)):
            return False

    for i in range(columns_number):
        row_digits = [board[j][i]
                      for j in range(rows_number) if board[j][i] in digits]
        if len(row_digits) != len(set(row_digits)):
            return False

        start_coordinates = [[0, 0], [0, 3], [0, 6], [
            3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

        for start_i, start_j in start_coordinates:
            elems = []

            for i in range(3):
                for j in range(3):
                    elems.append(board[start_i + i][start_j + j])

            square_digits = [elem for elem in elems if elem in digits]
            if len(square_digits) != len(set(square_digits)):
                return False

    return True
