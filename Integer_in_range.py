class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for number in range(left, right + 1):
            covered = False 
        
            for left, right in ranges:
                if number <= right and number >= left:
                    covered = True
                
            if covered == False:
                return False
        
        return True

        