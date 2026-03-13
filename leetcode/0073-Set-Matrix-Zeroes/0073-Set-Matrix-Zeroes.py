class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        rows = []
        cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.append(row)
                    cols.add(col)

        for row in rows:
            for col in range(len(matrix[row])):
                matrix[row][col] = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col in cols:
                    matrix[row][col] = 0