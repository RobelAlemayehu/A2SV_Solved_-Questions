class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        
        freq ={}
        res = []


        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key in freq:
            if freq[key] > n:
                res.append(key)


        return res