class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
         remainder_count = Counter({0: 1})
      
        result = 0
        prefix_sum = 0
      
        for num in nums:
            
            prefix_sum = (prefix_sum + num) % k
          
            result += remainder_count[prefix_sum]
          
            remainder_count[prefix_sum] += 1
      
        return result