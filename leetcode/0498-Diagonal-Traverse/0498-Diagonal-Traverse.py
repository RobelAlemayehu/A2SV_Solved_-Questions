class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        result = []
      
        for diagonal_index in range(rows + cols - 1):
            diagonal_elements = []

            start_row = 0 if diagonal_index < cols else diagonal_index - cols + 1
            start_col = diagonal_index if diagonal_index < cols else cols - 1
          
            current_row = start_row
            current_col = start_col
            while current_row < rows and current_col >= 0:
                diagonal_elements.append(mat[current_row][current_col])
                current_row += 1
                current_col -= 1
          
            if diagonal_index % 2 == 0:
                diagonal_elements = diagonal_elements[::-1]
          
            result.extend(diagonal_elements)
      
        return result