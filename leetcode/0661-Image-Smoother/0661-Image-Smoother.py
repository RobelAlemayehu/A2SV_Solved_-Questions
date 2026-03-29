class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
      
        result = [[0] * cols for _ in range(rows)]
      
        for row in range(rows):
            for col in range(cols):
                total_sum = 0
                cell_count = 0
              
                for neighbor_row in range(row - 1, row + 2):
                    for neighbor_col in range(col - 1, col + 2):
                        if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                            cell_count += 1
                            total_sum += img[neighbor_row][neighbor_col]
              
                result[row][col] = total_sum // cell_count
      
        return result