class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = Counter({0: 1})
      
        result = 0
        current = 0
      
        for num in nums:
            current += num
          
            result += prefix[current - k]
            prefix[current] += 1
      
        return result