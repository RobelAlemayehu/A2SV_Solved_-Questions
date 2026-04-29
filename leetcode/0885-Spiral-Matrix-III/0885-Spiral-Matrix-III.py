class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = [[rStart, cStart]]
        if rows * cols == 1:
            return result
      
        current_row = rStart
        current_col = cStart
      
        steps_count = 1
      
        while True:
            
            directions = [
                (0, 1, steps_count),      
                (1, 0, steps_count),      
                (0, -1, steps_count + 1), 
                (-1, 0, steps_count + 1)  
            ]
          
            for row_delta, col_delta, num_steps in directions:
                
                for _ in range(num_steps):
                    current_row += row_delta
                    current_col += col_delta
                  
                    
                    if 0 <= current_row < rows and 0 <= current_col < cols:
                        result.append([current_row, current_col])
                      
                       
                        if len(result) == rows * cols:
                            return result
          
            steps_count += 2