class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = set()

        res = []

        for num in nums:
            if num not in freq:
                freq.add(num)
            else:
                res.append(num)

        return res
    
        
        