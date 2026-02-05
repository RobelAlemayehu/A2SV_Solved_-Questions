class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = set()
        res = []

        for num in nums:
            if num in freq:
                res.append(num)
            else:
                freq.add(num)
        

        return res
        
        