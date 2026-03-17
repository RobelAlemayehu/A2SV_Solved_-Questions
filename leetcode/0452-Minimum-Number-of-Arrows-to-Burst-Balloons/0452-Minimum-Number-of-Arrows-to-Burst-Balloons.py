class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow = 0
        last = -inf 
        
        for a, b in sorted(points, key=lambda x: x[1]):
            if a > last:
                arrow += 1
                print(last)
                last = b

        return arrow